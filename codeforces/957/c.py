

import math
from collections import deque, defaultdict, Counter
import heapq


t = int(input())

for _ in range(t):

    n, m, k = list(map(int, input().split()))

    tail = [v for v in range(1, m+1)]
    head = [v for v in range(n, k-1, -1)]

    middle = [v for v in range(m+1, k)]

    ans = head+middle+tail
    print(" ".join(list(map(str, ans))))