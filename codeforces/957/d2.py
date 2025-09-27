

import math
from collections import deque, defaultdict, Counter
import heapq


t = int(input())

for _ in range(t):

    n, m, k = list(map(int, input().split()))
    info = list(input())

    curr = -1
    
    flag = False