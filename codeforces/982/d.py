

import math
from collections import deque, defaultdict, Counter
import bisect



t = int(input())


for _ in range(t):
    n, m = list(map(int, input().split()))
    alst = list(map(int, input().split()))
    blst = list(map(int, input().split()))

    if max(alst) > blst[0]:
        print(-1)
        continue

    dp = [[math.inf for _ in range(n)] for _ in range(m)]

    su = 0
    prefix = [0]
    for i in range(n):
        su += alst[i]
        prefix.append(su)

    rowmin = [math.inf for _ in range(n)]
    for bind in range(m):
        bk = blst[bind]

        for xind in range(n):
            curr = None
            if prefix[xind+1] <= bk:
                curr = min(m-bind-1, rowmin[xind]) 
                dp[bind][xind] = curr
            else:
                prevind = bisect.bisect_left(prefix, prefix[xind+1] - bk)
                curr = min(m-bind-1 + dp[bind][prevind-1], rowmin[xind])
                dp[bind][xind] = curr
        
            rowmin[xind] = min(rowmin[xind], dp[bind][xind])
    
    ans = math.inf
    for bind in range(m):
        ans = min(ans, dp[bind][-1])
        # print(dp[bind])
    print(ans)
    

                    


            


                
                


            


