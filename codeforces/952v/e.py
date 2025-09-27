

import heapq
import math
from collections import deque, defaultdict


t = int(input())

for _ in range(t):


    x, y, z, k = list(map(int, input().split()))
    ans = 0
    
    for a in range(1, x+1):
        if k%a != 0:
            continue
        for b in range(1, y+1):
            if k%(a*b) != 0:
                continue

            else:
                c = k //(a*b)
                if c > z:
                    continue

                curr = (x-a+1) * (y-b+1) * (z-c+1)
                ans = max(ans, curr)

    print(ans)
