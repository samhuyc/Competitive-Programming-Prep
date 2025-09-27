

import math
from collections import deque, defaultdict, Counter
import heapq


t = int(input())

for _ in range(t):
    n,a, b = list(map(int, input().split()))
    vals = list(map(int, input().split()))
    d = math.gcd(a, b)
    ans = 0

    vals = [v%d for v in vals]
    vals = list(set(vals))
    vals.sort()

    vals2 = [v+d for v in vals]
    vals = vals + vals2

    l, r = 0, 0

    while r < len(vals):
        diff = vals[r] - vals[l]
        if diff <= d/2:
            ans = max(ans, diff)
            r += 1
        else:
            l += 1
        
        
    
    print(ans)
    


