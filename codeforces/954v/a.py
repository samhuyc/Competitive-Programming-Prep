

import math
from collections import deque, defaultdict
import heapq


t = int(input())

for _ in range(t):


    vals = list(map(int, input().split()))
    vals.sort()
    print(abs(vals[0]-vals[1]) + abs(vals[2]-vals[1]))