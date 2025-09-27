
import heapq
import math
import re
from itertools import combinations, permutations, product, combinations_with_replacement
from collections import deque, defaultdict,Counter


def solve():
    ans = 0
    N, K = list(map(int, input().split()))

    mat = [list(input()) for _ in range(N)]

    quecount = 0
    
    rowf, rowl = None, None
    for x in range(N):
        if "1" in mat[:][x]:
            rowl = x
            if rowf == None:
                rowf = x
    
    colf, coll = None, None
    for y in range(N):
        if "1" in mat[y]:
            coll = y
            if colf == None:
                colf = y

    print(rowf, rowl)
    print(colf, coll)

    return ans


def main():
    t = int(input())
    for case in range(t):
        ans = solve()
        print(f"Case #{case+1}: {ans}")

main()