


import heapq
import math
import re
from collections import deque, defaultdict, Counter


t = int(input())


for _ in range(t):

    n = int(input())

    vals = list(map(int, input().split()))

    mat = [[[] for _ in range(n)]for _ in range(n-1)]

    for divisor in range(1, n):
        for i, v in enumerate(vals):
            mat[divisor-1][v%divisor].append(v)
    

    visited = {v:False for v in vals}


            
            



        

    