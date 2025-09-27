

from collections import deque, defaultdict
import heapq
import re
import math


t = int(input())

def calc(start, end, lst):
    score = 0
    carry = 0
    nxt = start

    l = False
    r = False

    for char in lst:
        if char == nxt:
            if char == start:
                l = True
            if char == end:
                r = True
            carry += 1
            nxt += 1
            nxt = nxt%5
            if char == end:
                score += carry
                carry = 0
    
    if l and r:
        return score - (len(lst)-score)
    else:
        return -math.inf


for _ in range(t):
    n, m = list(map(int, input().split()))
    info = []
    lookup = {'n':0,'a':1,'r':2,'e':3,'k':4}
    dp = [[0 for _ in range(5)] for _ in range(5)]
    for stringind in range(n):
        line = list(input())
        info = [lookup[char] for char in line if char in lookup]
        currvals = [[-math.inf for _ in range(5)] for _ in range(5)]
        for start in range(5):
            for end in range(5):
                currvals[start][end] = calc(start, end, info)

        newdp = [[dp[start][end] for end in range(5)] for start in range(5)]
        for start in range(5):
            for end in range(5):
                for prevend in range(5):
                    nowstart = (prevend + 1)%5
                    newdp[start][end] = max(newdp[start][end], dp[start][prevend] + currvals[nowstart][end])

        dp = newdp

    ans = 0
    for end in range(5):
        ans = max(ans, dp[0][end]-2*((end+1)%5))
    
    print(ans)



        
