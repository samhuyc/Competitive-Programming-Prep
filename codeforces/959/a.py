


import heapq
import math
import re
from collections import deque, defaultdict, Counter


t = int(input())


for _ in range(t):
    n, m = list(map(int, input().split()))
    mat = []
    for _ in range(n):

        row = list(map(int, input().split()))
        mat.append(row)
    
    if n == 1 and m == 1:
        print(-1)
        continue

    elif n > 1:
        newmat = []
        for i in range(-1, n-1):
            newmat.append(mat[i])
        mat = newmat
    
    else:
        for y in range(n):
            row = mat[y]
            curr = row[-1]
            for i in range(m):
                mat[y][i], curr = curr, mat[y][i]
    
    for row in mat:
        print(" ".join(list(map(str, row))))
    
    

