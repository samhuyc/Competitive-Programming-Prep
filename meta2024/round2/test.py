import heapq
import math
import re
from itertools import combinations, permutations, product, combinations_with_replacement

from collections import deque, defaultdict,Counter

def help(n, length, direction):
    digits = list(range(1, n + 1))
    if direction == 1:
        sequences = [''.join(map(str, comb)) for comb in combinations_with_replacement(digits, length)]
        return sequences
    else:
        sequences = []
        for comb in combinations_with_replacement(digits, length):
            mapped_comb = [n - d + 1 for d in comb]
            sequences.append(''.join(map(str, mapped_comb)))
        return sequences



def pre():
    tot = []
    for digits in range(18):
        if digits %2 == 0:
            continue

        onedigit = digits//2
        for middle in range(1, 10):
            left, right = help(middle-1, onedigit, 1), help(middle-1, onedigit, -1)
            for lseq in left:
                for rseq in right:
                    tot.append(int(lseq+str(middle)+rseq))
    return tot


def solve(tot):
    l, r, m = list(map(int, input().split()))
    ans = 0
    for v in tot:
        if v > r:
            break
        if v < l:
            continue
        if l <= v <= r and v % m == 0:
            ans += 1

    return ans


def main():
    t = int(input())
    tot = pre()
    print(tot[:100])
    for case in range(t):
        ans = solve(tot)
        print(f"Case #{case+1}: {ans}")

main()