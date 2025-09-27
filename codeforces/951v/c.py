
from collections import deque, defaultdict
import heapq
import math



t = int(input())

for _ in range(t):
    n = int(input())

    klst = list(map(int, input().split()))

    ans = []

    denom = 1
    for i in range(n):
        denom = math.lcm(denom, klst[i])
    
    for i in range(n):
        ans.append(denom//klst[i])
    
    if sum(ans) < denom:
        print(" ".join(list(map(str, ans))))
    else:
        print(-1)

