
from collections import defaultdict, deque, Counter
import math



t = int(input())


for _ in range(t):
    n = int(input())
    tops, bots = [False]*(n+1), [False]*(n+1)
    for _ in range(n):
        x, y = list(map(int, input().split()))
        if y == 0:
            bots[x] = True
        else:
            tops[x] = True

    ans = 0
    verts = 0
    for i in range(n+1):
        if bots[i] and tops[i] :
            verts += 1
        if i > 0 and i <= n:
            if bots[i] and tops[i-1] and tops[i+1]:
                ans += 1
            if tops[i] and bots[i-1] and bots[i+1]:
                ans += 1
    
    ans += verts*(n-2)
    print(ans)
    