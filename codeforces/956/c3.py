


import math
from collections import deque, defaultdict
import heapq


t = int(input())

for _ in range(t):

    n = int(input())
    alst = list(map(int, input().split()))
    blst = list(map(int, input().split()))
    clst = list(map(int, input().split()))

    tot = sum(alst)
    lim = tot//3 if tot%3 == 0 else math.ceil(tot/3)

    a, b, c = 0, 0, 0
    al, ar, bl, br, cl, cr = None, None, None, None, None, None

    asu = [0]
    bsu = [0]
    csu = [0]

    for i in range(n):
        a += alst[i]
        b += blst[i]
        c += clst[i]
        asu.append(a)
        bsu.append(b)
        csu.append(c)

    
    for i in range(n+1):
        if asu[i] >= lim:
            for j in range(i, n+1):
                if bsu[j]-bsu[i] >= lim and csu[-1]-csu[j]:
                    

