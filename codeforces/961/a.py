

from sys import stdin, stdout
import math
import re
import heapq
from collections import deque, Counter, defaultdict


t = int(input())

for _ in range(t):

    n, k = list(map(int, input().split()))
    ans = -1
    k += n
    curr = n
    while k > 0 and curr >= 0:
        if k >= curr*2:
            ans += 2
            k -= curr*2
            curr -= 1
        elif k > curr:
            ans += 2
            break
        elif k > 0:
            ans += 1
            break
        else:
            break
    
    print(ans)
            
        
            
        
    