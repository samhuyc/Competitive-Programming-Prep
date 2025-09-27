

from sys import stdin, stdout
import heapq
import re
import math
from collections import deque, defaultdict, Counter


t = int(input())


for _ in range(t):
    n = int(input())
    vals = list(map(int, input().split()))

    curr = vals[0]%2
    flag = True
    for v in vals:
        if v%2 != curr:
            flag = False
    
    if not flag:
        print(-1)
        continue

    k = 0
    res = []
    finished = False
    if sum(vals) == 0:
        print(0)
        print("")
        continue

    while k < 40:
        avg = (min(vals) + max(vals))//2
        for i in range(n):
            vals[i] = abs(vals[i] - avg)
        
        k += 1
        res.append(avg)
        if sum(vals) == 0:
            finished = True
            break
    
    if not finished:
        print(-1)
    else:
        print(k)
        # print(vals)
        print(" ".join(list(map(str, res))))
    
    







