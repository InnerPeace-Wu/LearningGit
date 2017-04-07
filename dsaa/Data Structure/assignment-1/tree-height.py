# python3

import sys, threading
#Import Queue
#import time

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class Node:
        def __init__(self, root):
                self.root = root
                self.children = []
        def addChild(self, child):
                self.children.append(child)

class TreeHeight:
        '''
        def __init__(self, n, parent):
                self.n = n
                self.parent = parent
        '''
        def read(self):
                self.n = int(sys.stdin.readline())
                self.parent = list(map(int, sys.stdin.readline().split()))

        def compute_height(self):
                # Replace this code with a faster implementation
                #st1 = time.time()
                nodes=[Node(i) for i in range(self.n)]
                root = -1
                for ci in range(self.n):
                        pi = self.parent[ci]
                        if pi == -1:
                                root = ci
                        else:
                                nodes[pi].addChild(nodes[ci])

                #q = Queue.Queue()
                q = []
                #q.put(nodes[root])
                q.append(nodes[root])
                pc, cc, h = 0, 1, 0
                #while not q.empty():
                while len(q):
                        #cnode = q.get()
                        cnode = q.pop(0)
                        cc -= 1
                        while len(cnode.children) > 0:
                                pc += 1
                                #q.put(cnode.children.pop())
                                q.append(cnode.children.pop())
                        if cc == 0:
                                h += 1
                                cc, pc = pc, 0
                #st2 = time.time()

                '''
                st2 = time.time()
                maxHeight = 0
                for vertex in range(self.n):
                        height = 0
                        i = vertex
                        while i != -1:
                                height += 1
                                i = self.parent[i]
                        maxHeight = max(maxHeight, height)

                st3 = time.time()
                return maxHeight
                '''
                #return (h, st1, st2)
                return h

def main():
        '''
        for i in range(1, 25):
                path = './tests/'
                if i < 10:
                        path += '0' + str(i)
                else:
                        path += str(i)
                with open(path, 'r') as f:
                        n = int(f.readline())
                        parent = list(map(int, f.readline().split()))
                tree = TreeHeight(n, parent)
                h1, t1, t2= tree.compute_height()
                patha = path + '.a'
                with open(patha, 'r') as a:
                        an = int(a.readline())
                if h1 ==  an:
                        print('ok', i, t2-t1)
                else:
                        print(h1, an)
        '''
        tree = TreeHeight()
        tree.read()
        print(tree.compute_height())

threading.Thread(target=main).start()
