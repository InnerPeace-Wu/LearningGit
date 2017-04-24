#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

def IsBinarySearchTree(tree):
  # Implement correct algorithm here
  if len(tree) < 2: return True
  keys = []
  previous = -float('inf')
  inorder(tree, keys, 0)
  for key in keys:
    try:
      if len(key) > 1: return False
    except:
      if previous > key: return False
    previous = key
  return True

def inorder(tree, keys, i):
  if tree[i][1] == -1 and tree[i][2] == -1:
    keys.append(tree[i][0])
    return tree[i][0]
  if tree[i][1] > 0:
    left = inorder(tree, keys, tree[i][1])
  else: left = -float('inf')
  if left >= tree[i][0]: keys.append((tree[i][0], -1))
  else: keys.append(tree[i][0])
  if tree[i][2] > 0: inorder(tree, keys, tree[i][2])
  return tree[i][0]

def main():
  nodes = int(sys.stdin.readline().strip())
  tree = []
  for i in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))
  if IsBinarySearchTree(tree):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
