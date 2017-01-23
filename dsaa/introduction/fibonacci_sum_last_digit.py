# Uses python3
import sys
import random

def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10

def fibonacci_sum_fast(n):
    if n <= 1:
        return n

    previous = 0
    current = 1
    sum = 1

    for _ in range(n - 1):
        previous, current = current,  (previous + current) % 10
        sum = (sum + current) % 10
    return sum

if __name__ == '__main__':

    while True:
        n = random.randint(0, 10000)
        print (n)
        r1 = fibonacci_sum_naive(n)
        r2 = fibonacci_sum_fast(n)
        if r1 == r2:
            print ("ok")
        else:
            print(r1)
            print(r2)
            break

    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_naive(n))
    print(fibonacci_sum_fast(n))
