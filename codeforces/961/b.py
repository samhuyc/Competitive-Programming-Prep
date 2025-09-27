

from sys import stdin, stdout
import math
import re
import heapq
from collections import deque, Counter, defaultdict


t = int(input())

def check(cv, cf, pv, pf, m):


    ans = cv * cf + pv * pf
    if ans <= m:
        return ans
    
    first = min(m//pv, pf)
    second = min((m - first*pv)//cv, cf)
    
    secondremain = min(cf - second, first)
    # print('*', pv, cv)
    # print(first, second, secondremain)
    ans = min(first * pv + second * cv + secondremain, m)

    return ans



def single(pv, pf, m):
    initial = m
    first_taken = min(pf,m//pv)
    m -= first_taken*pv
    return initial-m


for _ in range(t):
    n, m = list(map(int, input().split()))
    pedals = list(map(int, input().split()))
    counts = list(map(int, input().split()))

    info = [(pedals[i], counts[i]) for i in range(n)]
    info.sort(key=lambda x:x[0])

    ans = single(info[0][0], info[0][1], m)

    for i in range(1, len(info)):
        cv, cf = info[i]
        pv, pf = info[i-1]
        if cv - pv == 1:
            ans = max(ans, check(cv, cf, pv, pf, m))
        else:
            ans = max(ans, single(cv, cf, m))
    
    print(ans)
    



        