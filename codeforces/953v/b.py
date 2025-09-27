

import heapq
from collections import defaultdict, deque
import math



t = int(input())

for _ in range(t):
    n, a, b = list(map(int, input().split()))

    kmax = min(n, b)
    k = min(b+1-a, kmax) if b+1-a >0 else 0

    profit = ((b)+(b+1-k))*k//2 + (n-k)*a
    print(profit)


