

from sys import stdin, stdout
import math
import re
import heapq
from collections import deque, Counter, defaultdict


t = int(input())


for _ in range(t):
    n, m = list(map(int, input().split()))
    pedals = list(map(int, input().split()))
    pedals.sort()

    l, r = 0, 1
    ans = 0
    curr = pedals[0]

    while True:
        if curr > m:
            curr -= pedals[l]
            l += 1
            continue
        ans = max(curr, ans)
        # print(l, r)
        if r < n:
            while pedals[r] - pedals[l] > 1:
                curr -= pedals[l]
                l += 1

            curr += pedals[r]
            r += 1
        else:
            break
    print(ans)
                


    



        