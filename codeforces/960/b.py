


from sys import stdout
from collections import deque, defaultdict, Counter
import heapq
import re
import math


t = int(input())

for _ in range(t):
    n, p, s = list(map(int, input().split()))

    lst = [1] * n

    c = 0
    for i in range(p, n):
        if c % 2 == 0:
            lst[i] = -1
        else:
            lst[i] = 1
        c += 1
    
    d = 0
    for j in range(s-2, -1, -1):
        if d % 2 == 0:
            lst[j] = -1
        else:
            lst[j] = 1
        d += 1
    print(" ".join(list(map(str, lst))))




    