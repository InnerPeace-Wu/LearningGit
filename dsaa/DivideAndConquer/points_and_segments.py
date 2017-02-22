# Uses python3
import sys

def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    #write your code here
    starts = MergeSort(starts)
    ends = MergeSort(ends)
    for i in range(0, len(points)):
        st = BinarySearch(starts, points[i], 1)
        end = BinarySearch(ends, points[i], 0)
        cnt[i] = st - end
    return cnt

def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

def BinarySearch(a, x, direction): #with direction = 1, work for the 'starts' and 0 for the 'ends'
    if len(a) == 0:
        return -1
    left, right = 0, len(a)
    while left <= right:
        ave = (left + right) // 2
        if x == a[ave]:
            while x == a[ave]:
                if direction:  ave += 1
                else: ave -= 1
            if direction: return ave - 1
            else: return ave + 1
        elif x < a[ave]:
            right = ave - 1
        else:
            left = ave + 1
    return right + 1

def MergeSort(a):
    left, right = 0, len(a)
    if right - left <= 1:
        return a
    ave = (left + right) // 2
    sl = MergeSort(a[left:ave])
    sr = MergeSort(a[ave:right])
    return Merge(sl, sr)
def Merge(a, b):
    i, j = 0, 0
    c = []
    while i < len(a):
        if j == len(b):
            c += a[i:]
            break
        if a[i] == b[j]:
            c += 2*[a[i]]
            i += 1
            j += 1
        elif a[i] > b[j]:
            c.append(b[j])
            j += 1
        else:
            c.append(a[i])
            i += 1
    if j < len(b):
        c += b[j:]
    return c

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    cnt = naive_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
