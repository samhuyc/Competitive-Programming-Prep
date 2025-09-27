


import heapq
import math
import re
from collections import deque, defaultdict, Counter


t = int(input())


for _ in range(t):

    n, x = list(map(int, input().split()))
    tlst = list(map(int, input().split()))

    prefix = [0]
    su = 0
    for i in range(n):
        su += tlst[i]
        prefix.append(su)

    occur = [None] * n
    l, r = 0, 1
    su = 0
    while l < n+1 and r < n+1:
        # print(l, r)
        if prefix[r] - prefix[l] <= x:
            r += 1
        else:
            occur[l] = r-l-1
            l += 1
    
    for i in range(l, n):
        if occur[i] == None:
            occur[i] = n-i
    
    for i in range(n-1, -1, -1):
        base = occur[i]
        nxtind = i + base + 1
        if nxtind < n:
            base += occur[nxtind]
        occur[i] = base
    
    print(sum(occur))

        
    
    







