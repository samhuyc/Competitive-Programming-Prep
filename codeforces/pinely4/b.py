

from sys import stdin, stdout
import heapq
import re
import math
from collections import deque, defaultdict, Counter


t = int(input())


for _ in range(t):
    n = int(input())
    vals = list(map(int, input().split()))

    res = [0] * n

    for i in range(n-1):
        v = vals[i]
        res[i] = res[i] |v
        res[i+1] = res[i+1]|v
    
    flag = True
    for i in range(n-1):
        check = res[i+1] & res[i]
        if check != vals[i]:
            flag = False
    
    if not flag:
        print(-1)
    else:
        print(" ".join(list(map(str, res))))



