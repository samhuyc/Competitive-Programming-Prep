

from collections import deque, defaultdict
import heapq
import re
import math


t = int(input())

for _ in range(t):
    n, m, q = list(map(int, input().split()))
    teachers = list(map(int, input().split()))
    # teachers = [(i, v) for i, v in enumerate(teachers)]
    david = list(map(int, input().split()))
    david = [(i, v) for i, v in enumerate(david)]

    david.sort(key=lambda x:x[1])
    teachers.sort()

    ans = [None] * len(david)

    l, r = -1, teachers[0]
    tind = 0
    finished = False

    for dind, dpos in david:
        if not finished:
            while dpos > r:
                tind += 1
                if tind >= len(teachers):
                    finished = True
                    l, r = r, n
                    break
                else:
                    l, r = r, teachers[tind]
        
        if l == -1:
            ans[dind] = r-1
        elif finished:
            ans[dind] = n-l
        else:
            ans[dind] = (r-l)//2
    
    for a in ans:
        print(a)







