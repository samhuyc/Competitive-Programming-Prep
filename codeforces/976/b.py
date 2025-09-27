import math
import heapq
from collections import deque, defaultdict, Counter


t = int(input())



for _ in range(t):
    k = int(input())

    off = math.isqrt(k)

    while math.isqrt(k+off) + k < k+off:
        # print(off)
        off += 1
    
    print(math.isqrt(k+off) + k)
    