# Uses python3
import sys

def get_change(m):
    #write your code here
    count = int(m / 10)
    remain = m % 10
    count += int(remain / 5)
    remain = remain % 5
    count += remain
    return count

if __name__ == '__main__':
    m = int(sys.stdin.read())
    #l = [12, 2, 28, 123, 2312, 3453]
    #for m in l:
    print(get_change(m))
