#Uses python3

import sys

def reach(adj, x, y):
    #write your code here
    re = 0
    if x >= len(adj) or x < 0:
        return 0
    if y in adj[x]:
        return 1
    adj[x].append('t')
    for w in adj[x][:-1]:
        if len(adj[w]) > 0 and adj[w][-1] != 't':
            re = reach(adj, w, y)
            if re: break
    if re: return 1
    else: return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1
    #print(edges)
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    #print(adj)
    print(reach(adj, x, y))
