
import math
import heapq
import re
from collections import deque, defaultdict



t = int(input())


for _ in range(t):
    n = int(input())
    vals = list(map(int, input().split()))

    vals.sort()
    print(vals[len(vals)//2])