import math
import heapq
from collections import deque, defaultdict, Counter


t = int(input())


for _ in range(t):
    b, c, d = list(map(int, input().split()))

    bad = False
    a = 0
    for ind in range(61):
        
        bi = (b >> ind)&1
        ci = (c >> ind)&1
        di = (d >> ind)&1

        if bi == 0 and ci == 0:
            if di == 1:
                ai = 1
            else:
                ai = 0
        elif bi == 1 and ci == 1:
            if di == 0:
                ai = 1
            else:
                ai = 0
        elif bi == 1 and ci == 0:
            if di == 0:
                bad = True
                break
            else:
                ai = 0
        else:
            if di == 1:
                bad = True
                break
            else:
                ai = 0

        if not bad:
            a = a| (ai << ind)
    
    if bad:
        print(-1)
    else:
        print(a)
