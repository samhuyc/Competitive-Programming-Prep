

import math
from collections import deque, defaultdict, Counter
import heapq


t = int(input())

for _ in range(t):

    n, m, k = list(map(int, input().split()))
    info = list(input())

    curr = -1
    
    flag = False

    while True:
        
        if k < 0:
            break

        if curr+1+m > n:
            flag = True
            break
        
        jumped = False
        lastwater = None
        for i in range(curr+1, curr+1+m):
            if info[i] == "L":
                curr = i
                jumped = True
                break
            elif info[i] == "W":
                lastwater = i
        
        if jumped:
            continue

        if lastwater == None:
            break
        
        curr = lastwater
        while k > 0:
            curr += 1
            k -= 1
            if curr >= n:
                flag = True
                break
            if info[curr] == "C":
                break

            if info[curr] == "L":
                break
        
        if flag:
            break

        if info[curr] != "L":
            break

    
    if flag:
        print("Yes")
    else:
        print("No")

