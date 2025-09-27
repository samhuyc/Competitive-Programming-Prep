


import heapq
import math
import re
from collections import deque, defaultdict, Counter


t = int(input())


for _ in range(t):
    n = int(input())
    s, t = list(map(int, list(input()))), list(map(int, list(input())))

    prevone = False
    flag = True
    for i in range(n):
        si, ti = s[i], t[i]
        if si == 1:
            prevone = True

        if si == 0 and ti == 1 and not prevone:
            flag = False
            break
    
    if flag:
        print('YES')
    else:
        print('NO')

