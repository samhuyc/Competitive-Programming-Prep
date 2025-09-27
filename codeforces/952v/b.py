

import heapq
import math
from collections import deque, defaultdict


t = int(input())

for _ in range(t):

    n = int(input())
    best = 0
    candidate = None

    for x in range(2, n+1):
        curr = 0
        c = 1
    
        while c*x <= n:
            curr += c*x
            c += 1
        
        if curr > best:
            candidate = x
            best = curr


    
    print(candidate)
        

            
            