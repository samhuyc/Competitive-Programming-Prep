

import math
from collections import deque, defaultdict, Counter
import heapq


t = int(input())

for _ in range(t):
    l, r = list(map(int, input().split()))
    visited = [(v, False) for v in range(l, r+1)]
    n = len(visited)

    ans = 0

    while True:
        
        f, s, t = None, None, None
        for i in range(n):
            v, bo = visited[i]
            if bo == False:
                f = v
                visited[i] = (v, True)
                break
        if f == None:
            break
        
        for j in range(i+1, n):
            v, bo = visited[j]
            if bo == False and math.gcd(f, v) == 1:
                s = v
                break
        if s == None:
            continue

        for k in range(j+1, n):
            v, bo = visited[k]
            if bo == False and math.gcd(f, v) == 1 and math.gcd(s, v) == 1:
                ans += 1
                visited[j] = (s, True)
                visited[k] = (v, True)
                # print(f, s, v)
                break
        
    print(ans)

        
        