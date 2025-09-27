

import math
from collections import deque, defaultdict
import heapq


t = int(input())

for _ in range(t):

    
    n, k = list(map(int, input().split()))
    alst = list(map(int, input().split()))
    remain = [(v, v%k) for v in alst]

    remain.sort(key=lambda x:x[1])

    counter = 0
    curr = remain[0][1]
    flag = 0

    for v, r in remain:
        if r == curr:
            counter += 1
        else:
            if counter %2 != 0:
                flag +=1

            counter = 1
            curr = r
    
    if n%2 == 1 and flag > 1:
        print(-1)
        continue
    elif n%2 == 0 and flag > 0:
        print(-1)
        continue

    remaingroup = []
    currgroup = []
    curr = remain[0][1]

    for v, r in remain:
        if r == curr:
            currgroup.append(v)
        else:
            remaingroup.append(currgroup)
            currgroup = [v]
            curr = r
    
    if currgroup:
        remaingroup.append(currgroup)
    
    ans = 0
    for group in remaingroup:
        gp = sorted(group)
        if len(gp) % 2 == 0:
            for i in range(0, len(gp), 2):
                ans += (gp[i+1] - gp[i])//k
        elif len(gp) == 1:
            ans += 0
        else:
            

    
    print(ans)







