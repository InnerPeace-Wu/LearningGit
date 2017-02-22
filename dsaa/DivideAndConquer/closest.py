#Uses python3
import sys
import math
#import functools

def minimum_distance(x, y):
    #write your code here
    assert len(x) == len(y), "Error with the cordinates of the points"
    points = sorted(zip(x, y), key=lambda t:t[0])
    return distance(points)

def distance(x):
    if len(x) == 2:
        return dis(x[0], x[1])
    elif len(x) == 1:
        return -1
    mid = len(x) // 2
    Ldis = distance(x[0:mid])
    Rdis = distance(x[mid:])
    if Ldis * Rdis < 0: td = abs(Ldis * Rdis) #or return -Ldis * Rdis
    else: td = min(Ldis, Rdis)
    for lpoint in x[0:mid]:
        for rpoint in x[mid:]:
            if rpoint[0] - lpoint[0] > td or abs(rpoint[1] - lpoint[1]) > td:
                break
            td = min(td, dis(lpoint, rpoint))
    return td

def dis(a, b):
    return math.sqrt(power2(a[0]-b[0]) + power2(a[1]-b[1]))

def power2(x):
    return x*x
if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
