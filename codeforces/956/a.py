


import math
from collections import deque, defaultdict
import heapq


t = int(input())

for _ in range(t):

    n = int(input())

    ans = [v for v in range(1, n+1)]

    print(" ".join(list(map(str, ans))))