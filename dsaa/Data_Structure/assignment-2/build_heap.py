# python3

class HeapBuilder:
  def __init__(self):
    self._swaps = []
    self._data = []

  def ReadData(self):
    n = int(input())
    self._data = [int(s) for s in input().split()]
    assert n == len(self._data)

  def WriteResponse(self):
    print(len(self._swaps))
    for swap in self._swaps:
      print(swap[0], swap[1])

  def GenerateSwaps(self):
    # The following naive implementation just sorts 
    # the given sequence using selection sort algorithm
    # and saves the resulting sequence of swaps.
    # This turns the given array into a heap, 
    # but in the worst case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    for i in range(len(self._data)):
      for j in range(i + 1, len(self._data)):
        if self._data[i] > self._data[j]:
          self._swaps.append((i, j))
          self._data[i], self._data[j] = self._data[j], self._data[i]

  def Solve(self):
    self.ReadData()
    #self.GenerateSwaps()
    self.Generate_swaps()
    self.WriteResponse()

  '''
  author = InnerPeace
  '''
  @staticmethod
  def parent(i):
    return (i - 1) // 2
  @staticmethod
  def left_child(i):
    return 2*i + 1
  @staticmethod
  def right_child(i):
    return 2*(i+ 1)


  def sift_up(self, i):
    while i > 0 and self._data[parent(i)] > self._data[i]:
      self._data[parent(i)], self._data[i] = self._data[i], self._data[parent(i)]

  def sift_down(self, i):
    min_index = i
    n = len(self._data)
    while True:
      l, r = self.left_child(i), self.right_child(i)
      if l < n and self._data[l] < self._data[min_index]:
        min_index = l
      if r < n and self._data[r] < self._data[min_index]:
        min_index = r
      if min_index == i:
        break
      else:
        self._data[i], self._data[min_index] = self._data[min_index], self._data[i]
        self._swaps.append((i, min_index))
        i = min_index

  def Generate_swaps(self):
    n = len(self._data)
    i = n // 2
    while i > -1:
      self.sift_down(i)
      i -= 1

if __name__ == '__main__':
    '''
    path = './tests/04'
    heap_test = HeapBuilder()
    with open(path, 'r') as data:
      n = data.readline().strip()
      heap_test._data = list(map(int, data.readline().split()))
    heap_test.Generate_swaps()
    heap_test.WriteResponse()
    pathan = './tests/04.a'
    re = []
    with open(pathan, 'r') as an:
      re_n = an.readline().strip()
      while an.readline() != '':
        re.append(tuple(map(int, an.readline().split())))
    print(re)
    '''
    heap_builder = HeapBuilder()
    heap_builder.Solve()
