

import heapq
from collections import defaultdict, deque
import math



t = int(input())

for _ in range(t):
    n = int(input())
    pages = list(map(int, input().split()))
    print(max(pages[:-1]) + pages[-1])




