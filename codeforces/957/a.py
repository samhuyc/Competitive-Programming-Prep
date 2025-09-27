

import math
from collections import deque, defaultdict, Counter
import heapq


t = int(input())

for _ in range(t):


    a, b, c = list(map(int, input().split()))

    for _ in range(5):
        if a*b >= a*c and a*b >= b*c:
            c += 1
        elif b*c >= a*b and b*c >= a*c:
            a += 1
        else:
            b += 1
        
    print(a*b*c)