

import heapq
import math
from collections import deque, defaultdict


t = int(input())

def check(turn):
    total = 0
    for i in range(n):
        a, c = attack[i], cd[i]

        total += ((turn- 1)//c+1)*a
        if total >= h:
            # print(turn, total)
            return True
    
    return False

for _ in range(t):

    h, n = list(map(int, input().split()))
    attack = list(map(int, input().split()))
    cd = list(map(int, input().split()))


    l, r = 1, h*(min(cd)+1)
    ans = None

    while l <= r:
        mid = (l+r)//2
        curr = check(mid)
        prev = check(mid-1)

        if curr and prev:
            r = mid-1
        elif (not curr) and (not prev):
            l = mid+1
        else:
            ans = mid
            break
    
    print(ans)







        