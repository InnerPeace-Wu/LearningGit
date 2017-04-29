# Uses python3
'trying to work with stress testing'

__author__ = 'InnerPeace'

import random
import argparse

#naive solution
def maxpairwiseproduct(n, a):
    assert len(a) == n, "the length of the list is not equal to n = %r" % n
    assert n >= 2, "'n' should be great or equal than 2"
    result = 0
    for i in range(0, n):
        for j in range(i+1, n):
            if a[i]*a[j] > result:
                result = a[i]*a[j]

    return result

#faster vision of solution
def maxpairwiseproductfast(n, a):
    #assert(len(a) ==  n)
    assert len(a) == n, "the length of the list is not equal to n = %r" % n
    assert n >= 2, "'n' should be great or equal than 2"
    #assert(n >= 2)
    max1 = -1
    max2 = -1
    for i in range(0, n):
        if max1 == -1:
            max1 = i
        elif a[i] >= a[max1]:
            max2 = max1
            max1 = i
        elif max2 == -1 or a[max2] < a[i]:
            max2 = i
    return a[max1] * a[max2]


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("-st", "-stress-test", help="run the stress testing", action="store_true")
    args = parser.parse_args()
    if args.st:
        while True:
            n = random.randint(0, 1000) + 2
            print (n)
            a = []
            for i in range(0, n):
                a.append(random.randint(0, 10000))
            print (a)

            res1 = maxpairwiseproductfast(n, a)
            res2 = maxpairwiseproduct(n, a)

            if res2 != res1:
                print ('wrong answer: %d, %d' % (res1, res2))
                break
            else:
                print ("ok")
    else:
        n = int(input())
        a = [int(x) for x in input().split()]
        print (maxpairwiseproductfast(n, a))
        #print (maxpairwiseproduct(n, a))
