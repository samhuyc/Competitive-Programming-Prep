

import math
from collections import deque, defaultdict, Counter
import heapq


t = int(input())

for _ in range(t):
    n, k = list(map(int, input().split()))
    cakes = list(map(int, input().split()))

    oners = cakes.count(1)
    ma = max(cakes)
    cutting = n - ma - oners - (k-1-oners)

    adding = n - ma
    print(cutting+ adding)