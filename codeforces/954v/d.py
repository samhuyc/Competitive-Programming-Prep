

import math
from collections import deque, defaultdict
import heapq


t = int(input())

for _ in range(t):

    n = int(input()) 
    vals = list(map(int, list(input())))

    if len(vals) == 2:
        print(int(str(vals[0])+str(vals[1])))
        continue

    if len(vals) == 3:
        a, b, c = vals
        curr = (10*a + b)*c
        curr = min(curr, (10*a + b)+c)
        curr = min(curr, a + (10*b+c))
        curr = min(curr, a * (10*b+c))
        print(curr)
        continue
    if 0 in vals:
        print(0)
        continue

    ans = 0
    for i in range(n):
        if vals[i] != 1:
            ans += vals[i]
    
    res = None

    for i in range(1, n):
        first = vals[i-1]
        second = vals[i]
        if res == None:
            curr = ans + first * 10 + second
            if first != 1:
                curr -= first
            if second != 1:
                curr -= second

            res = curr
        else:
            curr = ans + first * 10 + second
            if first != 1:
                curr -= first
            if second != 1:
                curr -= second

            res = min(res, curr)
    
    print(res)
        
    
