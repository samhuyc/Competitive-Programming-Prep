


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
    info = info[::-1]

    
    survival = []
    for v, freq in info:
        survival.append([v, freq])
    
    currsum = sum(process)

    
    while True:
        # print(survival)
        if survival == []:
            break

        total += currsum
        missed = 0
        newsurvival = []

        for v, freq in survival:
            if freq == 1:
                currsum -= v
                missed += 1
            elif freq > 1:
                currsum += (missed-1)*v
                newsurvival.append([v, freq-1+missed])
                missed = 1
        
        survival = newsurvival

    
    print(total)




