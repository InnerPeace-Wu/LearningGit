# Uses python3
import sys
import random

def fibonacci_partial_sum_naive(from_, to):
    if to <= 1:
        return to

    previous = 0
    current  = 1

    for _ in range(from_ - 1):
        previous, current = current, previous + current

    sum = current
    if from_ == 0:
        from_ = 1
    for _ in range(to - from_):
        previous, current = current, previous + current
        sum += current

    return sum % 10

def fibonacci_partial_sum_fast(from_, to):
    if to <= 1:
        return to
    sum = 0
    if from_ <= 1:
        sum = 1
    previous = 0
    current = 1

    for _ in range(to - 1):
        previous, current = current, (previous + current) % 10
        if _ + 2 >= from_:
            sum = (sum + current) % 10
    return sum

if __name__ == '__main__':
    while True:
        n = random.randint(0, 10000)
        m = random.randint(0, 10000) + n
        print ("n: %d, m: %d" % (n, m))
        r1 = fibonacci_partial_sum_naive(n, m)
        r2 = fibonacci_partial_sum_fast(n, m)
        if r1 == r2:
            print ("ok")
        else:
            print(r1)
            print(r2)
            break
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    from_ = 0
    to = 2
    print(fibonacci_partial_sum_naive(from_, to))
    print(fibonacci_partial_sum_fast(from_, to))
