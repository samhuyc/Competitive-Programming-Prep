


from sys import stdout
from collections import deque, defaultdict, Counter
import heapq
import re
import math


t = int(input())

for _ in range(t):
    n = int(input())
    vals = list(map(int, input().split()))

    hp = []
    dic = {}
    curr = 0

    process = []

    for v in vals:
        if v not in dic:
            dic[v] = 0
        dic[v] += 1

        if dic[v] >= 2 and v > curr:
            process.append(v)
            curr = v
        else:
            process.append(curr)
    
    total = sum(vals)

    info = list(dict(Counter(process)).items())
    info.sort(key=lambda x:x[0])
    info = info[1:]
    
    print(process)
    print(info)

    survival = {0:0}
    prev = 0

    for v, freq in info:
        if freq == 1:
            survival[prev] += 1
            survival[v] = 1
        else:
            survival[v] = freq
            prev = v
    
    for v, days in survival.items():
        total += (days*(days+1)//2)*v
    
    print(survival)
    print(total)





    