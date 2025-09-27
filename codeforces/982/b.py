

import math
from collections import deque, defaultdict, Counter



t = int(input())


for _ in range(t):
    n = int(input())
    vals = list(map(int, input().split()))
    dp = [0 for _ in range(n)]

    ans = 0
    for i in range(n-1, -1, -1):
        curr = 0
        for j in range(i, n):
            if vals[i] >= vals[j]:
                curr += 1
        ans = max(ans, curr)
    
    print(n-ans)

