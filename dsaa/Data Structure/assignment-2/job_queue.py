# python3
#import fire
import time

class JobQueue:
    def read_data(self):
        '''
        path = './Programming-Assignment-2/job_queue/tests/08'
        with open(path, 'r') as data:
            self.num_workers, m = map(int, data.readline().split())
            self.jobs = list(map(int, data.readline().split()))
        '''
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        '''
        self.num_workers, m = 1000, 10000
        self.jobs = [1 for i in range(m)]
        '''
        assert m == len(self.jobs)

    def write_response(self):
        for i in range(len(self.jobs)):
          print(self.assigned_workers[i], self.start_times[i]) 

    def assign_jobs(self):
        # TODO: replace this code with a faster algorithm.
        self.assigned_workers = [None] * len(self.jobs)
        self.start_times = [None] * len(self.jobs)
        #new code
        self._response = []
        temp_worker = []
        for i in range(self.num_workers):
            temp_worker.append([i, 0])
        self._free_time = PriorityQueue(temp_worker, ('multi', 1), mode = 0, dim = "TWO")
        for job in self.jobs:
#           print(self._free_time._heap)
            worker = self._free_time.get()
            self._response.append(tuple(worker))
            worker[1] += job
            self._free_time.change_priority(0, worker[1])
#            print(self._free_time._heap)

        '''
        next_free_time = [0] * self.num_workers
        for i in range(len(self.jobs)):
          next_worker = 0
          for j in range(self.num_workers):
            if next_free_time[j] < next_free_time[next_worker]:
              next_worker = j
          self.assigned_workers[i] = next_worker
          self.start_times[i] = next_free_time[next_worker]
          next_free_time[next_worker] += self.jobs[i]
        '''

    def job_assign(self):
        temp_worker = []
        for i in range(self.num_workers):
            temp_worker.append([i, 0])
        self._worker_queue = PriorityQueue(temp_worker, ('multi', 0), 0)
        self._time_queue = PriorityQueue([], ('multi', 1), 0)
        self._response = []
        #if num_workers == 0?
        for job in self.jobs:
            if self._worker_queue._size == 0:
                extracted_worker = self._time_queue.heap_extract()
                self._worker_queue.heap_insert(extracted_worker)
                while self._time_queue._size > 0 and  extracted_worker[1] == self._time_queue.get()[1]:
                    self._worker_queue.heap_insert(self._time_queue.heap_extract())
            worker = self._worker_queue.heap_extract()
            self._response.append(tuple(worker))
            worker[1] += job
            self._time_queue.heap_insert(worker)
#            print("time", self._time_queue._heap)
#            print('work', self._worker_queue._heap)
#            print('res', self._response)

    def response_write(self):
        for i in self._response:
            print(i[0], i[1])
    def solve(self):
        self.read_data()
        if self.num_workers == 0:
            return None
        '''
        self.assign_jobs()
        self.write_response()
        '''
        #self.time1 = time.time()
        #self.job_assign()
        self.assign_jobs()
        #self.time2 =time.time()
        self.response_write()
        '''
        an_path = './an'
        with open(an_path, 'w') as an:
            an.write(str(self._response))
        '''

class PriorityQueue:
    def __init__(self, data = [], key = ('default', -1), mode = 1, dim = 'ONE'): #mode=1, max-heap; else, min-heap
        self._mode = mode
        self._key = key
        self._size = len(data)
        self._heap = data
        self._dim = dim
        self._build_heap()

    @staticmethod
    def _parent(i):
        return (i -1) // 2
    @staticmethod
    def _left_child(i):
        return 2 * i + 1
    @staticmethod
    def _right_child(i):
        return 2 * (i + 1)

    def _get_parent(self, i):
        if self._key[0] == 'multi': #multi-element
            return self._heap[self._parent(i)][self._key[1]]
        else:
            return self._heap[self._parent(i)]

    def _get_current(self, i):
        if self._key[0] == 'multi':
            return self._heap[i][self._key[1]]
        else:
            return self._heap[i]

    def _set_current(self, i, p):
        if self._key[0] == 'multi':
            self._heap[i][self._key[1]] = p
        else:
            self._heap[i] = p

    def _sift_up(self, i):
        if not self._mode: #min-heap
            while i > 0 and self._get_parent(i) >= self._get_current(i):
                if self._dim == "TWO" and self._get_parent(i) == self._get_current(i):
                    if sum(self._heap[self._parent(i)]) > sum(self._heap[i]):
                        self._heap[self._parent(i)], self._heap[i] = self._heap[i], self._heap[self._parent(i)]
                        i = self._parent(i)
                elif self._get_parent(i) > self._get_current(i):
                    self._heap[self._parent(i)], self._heap[i] = self._heap[i], self._heap[self._parent(i)]
                    i = self._parent(i)
        else:#max-heap
            while i > 0 and self._get_parent(i) < self._get_current(i):
                self._heap[self._parent(i)], self._heap[i] = self._heap[i], self._heap[self._parent(i)]
                i = self._parent(i)

    def _sift_down(self, i):
        if self._mode: #max-heap
            max_index = i
            while True:
                l, r = self._left_child(i), self._right_child(i)
                if l < self._size and self._get_current(l) > self._get_current(max_index):
                    max_index = l
                if r < self._size and self._get_current(r) > self._get_current(max_index):
                    max_index = r
                if max_index == i:
                    break
                else:
                    self._heap[i], self._heap[max_index] = self._heap[max_index], self._heap[i]
                    i = max_index
        else: #min-heap
            min_index = i
            while True:
                l, r = self._left_child(i), self._right_child(i)
                if l < self._size and self._get_current(l) < self._get_current(min_index):
                    min_index = l
                elif l < self._size and self._get_current(l) == self._get_current(min_index):
                    if self._dim == "TWO" and sum(self._heap[l]) < sum(self._heap[min_index]):
                        min_index = l

                if r < self._size and self._get_current(r) < self._get_current(min_index):
                    min_index = r
                elif r < self._size and self._get_current(r) == self._get_current(min_index):
                    if self._dim == "TWO" and sum(self._heap[r]) < sum(self._heap[min_index]):
                        min_index = r
                if min_index == i:
                    break
                else:
                    self._heap[i], self._heap[min_index] = self._heap[min_index], self._heap[i]
                    i = min_index

    def _build_heap(self):
        i = self._size // 2
        while i > -1:
            self._sift_down(i)
            i -= 1

    def heap_insert(self, p):
        self._size += 1
        self._heap.append(p)
        self._sift_up(self._size - 1)

    def heap_extract(self):
        result = self._heap[0]
        self._heap[0] = self._heap[self._size - 1]
        self._heap.pop(-1)
        self._size -= 1
        self._sift_down(0)
        return result

    def get(self):
        return self._heap[0]

    def change_priority(self, i, p):
        old_priority = self._get_current(i)
        self._set_current(i, p)
        if self._mode: #max-heap
            if old_priority < p:
                self._sift_up(i)
            else:
                self._sift_down(i)

        else:
            if old_priority > p:
                self._sift_up(i)
            else:
                self._sift_down(i)


if __name__ == '__main__':
    #test...
    '''
    #fire.Fire(PriorityQueue)
    a =[(1, 2), (3, 4), (2, 1), (5, 7)]
    queue = PriorityQueue(a, ('multi', 1))
    print(queue._heap)
    print(queue.heap_extract())
    print(queue._heap)
    print(queue.heap_insert((7, 8)))
    print(queue._heap)
    print(queue.heap_extract())
    print(queue._heap)
    #test...
    '''
    job_queue = JobQueue()
    job_queue.solve()
    #print(job_queue.time2 - job_queue.time1)
