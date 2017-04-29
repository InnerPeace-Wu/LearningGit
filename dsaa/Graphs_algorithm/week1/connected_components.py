#Uses python3

import sys


def number_of_components(adj):
    result = 1
    #write your code here
    if len(adj) <= 1:
        return len(adj)
    for i in range(len(adj)):
        if len(adj[i]) == 0:
            adj[i].append('t')
        if adj[i][-1] != 't':
            explore(adj, i)
            result += 1
    return result

def explore(adj, x):
    adj[x].append('t')
    for w in adj[x][:-1]:
        if adj[w][-1] != 't':
            explore(adj, w)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(number_of_components(adj))
