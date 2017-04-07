# python3

import sys
'''
#testing
path = './Programming-Assignment-2/merging_tables/tests/116'
data = open(path, 'r')
n, m = map(int, data.readline().split())
lines = list(map(int, data.readline().split()))
#
'''
n, m = map(int, sys.stdin.readline().split())
lines = list(map(int, sys.stdin.readline().split()))
rank = list(tuple(lines))
#rank = [1] * n
parent = list(range(0, n))
ans = max(lines)

def getParent(table):
    # find parent and compress path
    if table != parent[table]:
        parent[table] = getParent(parent[table])
    return parent[table]

def merge(destination, source):
    realDestination, realSource = getParent(destination), getParent(source)

    if realDestination == realSource:
        return -1

    # merge two components
    # use union by rank heuristic 
    # update ans with the new maximum table size
    if rank[realDestination] >= rank[realSource]:
        parent[realSource] = realDestination
        rank[realDestination] += rank[realSource]
        rank[realSource] = 0
        return rank[realDestination]
    else:
        parent[realDestination] = realSource
        rank[realSource] += rank[realDestination]
        rank[realDestination] = 0
        return rank[realSource]

for i in range(m):
    destination, source = map(int, sys.stdin.readline().split())
    #testing
    #destination, source = map(int, data.readline().split())
    an = merge(destination - 1, source - 1)
    if an > ans: ans = an
#    print(parent)
#    print(rank)
    print(ans)

#testing
#data.close()
