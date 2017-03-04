# python3

class Request:
    def __init__(self, arrival_time, process_time):
        self.arrival_time = arrival_time
        self.process_time = process_time

class Response:
    def __init__(self, dropped, start_time):
        self.dropped = dropped
        self.start_time = start_time

class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time_ = []

    def Process(self, request):
        # write your code here
        if self.size == 0:
            return Response(True, -1)
        lenth = len(self.finish_time_)
        if lenth == 0:
            self.finish_time_.append(request.arrival_time+request.process_time)
            return Response(False, request.arrival_time)
        elif lenth == size:
            if self.finish_time_[0] <= request.arrival_time:
                start_time = self.finish_time_[-1]
                self.finish_time_.append(start_time+request.process_time)
                self.finish_time_.pop(0)
                return Response(False,start_time)
            else:
                return Response(True, -1)
        else:
            start_time = self.finish_time_[-1]
            self.finish_time_.append(start_time+request.process_time)
            return Response(False,start_time)

def ReadRequests(count):
    requests = []
    for i in range(count):
        arrival_time, process_time = map(int, input().strip().split())
        requests.append(Request(arrival_time, process_time))
    return requests
###for testing
def ReadRequestsfromFile(files, count):
    requests = []
    for i in range(count):
        arrival_time, process_time = map(int, files.readline().split())
        requests.append(Request(arrival_time, process_time))
    return requests
###testing

def ProcessRequests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.Process(request))
    return responses

def PrintResponses(responses):
    for response in responses:
        print(response.start_time if not response.dropped else -1)

if __name__ == "__main__":
    ### Testing
    for p in range(1, 23):
        path = './Programming-Assignment-1/network_packet_processing_simulation/tests/'
        if p < 10:
            path += '0' + str(p)
        else:
            path += str(p)
        with open(path, 'r') as f:
            size, count = map(int, f.readline().split())
            requests = ReadRequestsfromFile(f, count)
            buff = Buffer(size)
            responses = ProcessRequests(requests, buff)
        patha = path + '.a'
        with open(patha,"r") as fa:
            ans = map(int, fa.readline().strip())
        results = []
        for res in responses:
            re = res.start_time if not res.dropped else -1
            results.append(re)
        i = 0
        for an in ans:
            if results[i] == an:
                print("%d, ok" % p)
            else:
                print("error, %d" % p)
                break
            i += 1
    print("all done")
    ### Testing

    size, count = map(int, input().strip().split())
    requests = ReadRequests(count)

    buffer = Buffer(size)
    responses = ProcessRequests(requests, buffer)

    PrintResponses(responses)
