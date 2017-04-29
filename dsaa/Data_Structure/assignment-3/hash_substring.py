# python3
import random

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    return [
        i 
        for i in range(len(text) - len(pattern) + 1) 
        if text[i:i + len(pattern)] == pattern
    ]

def poly_hash(string, prime, multiplier):
    ans = 0
    for s in reversed(string):
        ans = (ans * multiplier + ord(s)) % prime
    return ans

def precompute_hashs(pattern, text, prime, multiplier):
    lt, lp = len(text), len(pattern)
    Hash_all = [0] * (lt - lp + 1)
    #print(Hash_all, lt, lp)
    Hash_all[lt -lp] = poly_hash(text[lt-lp : ], prime, multiplier)
    temp = 1
    for i in range(lp):
        temp = (temp * multiplier) % prime

    for i in reversed(range(lt - lp)):
        Hash_all[i] = (multiplier * Hash_all[i + 1] + ord(text[i]) -
                       temp * ord(text[i + lp])) % prime

    return Hash_all

def are_equal(pattern, text):
    if len(text) != len(pattern): return False
    for i in range(len(pattern)):
        if text[i] != pattern[i]: return False
    return True

def rabinkarp(pattern, text):
    lt, lp = len(text), len(pattern)
    if lt < lp: return -1
    prime = 500007
    #multiplier = 263
    multiplier = random.randint(1, prime - 1)
    result = []
    hash_p = poly_hash(pattern, prime, multiplier)
    Hash_all = precompute_hashs(pattern, text, prime, multiplier)
    #print(Hash_all, hash_p)
    for i in range(len(text) - len(pattern) + 1):
        if Hash_all[i] == hash_p and text[i : i + lp] == pattern:
            result.append(i)

    return result

if __name__ == '__main__':
    #print_occurrences(get_occurrences(*read_input()))
    print_occurrences(rabinkarp(*read_input()))
