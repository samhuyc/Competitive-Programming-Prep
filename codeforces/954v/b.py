


import math
from collections import deque, defaultdict
import heapq


t = int(input())

for _ in range(t):

    n, m = list(map(int, input().split()))

    mat = []
    for _ in range(n):
        row = list(map(int, input().split()))
        mat.append(row)

    while True:
        flag = False
        for i in range(n):
            for j in range(m):
                curr = mat[i][j]
                ma = 0
                if i > 0:
                    ma = max(ma, mat[i-1][j])
                if i < n-1:
                    ma = max(ma, mat[i+1][j])
                if j > 0:
                    ma = max(ma, mat[i][j-1])
                if j < m-1:
                    ma = max(ma, mat[i][j+1])
                # ma = max(mat[i-1][j], mat[i+1][j], mat[i][j-1], mat[i][j+1])
                # mi = max(mat[i-1][j], mat[i+1][j], mat[i][j-1], mat[i][j+1])

                if curr > ma:
                    mat[i][j] = ma
                    flag = True
            
        if not flag:
            break
    
    for i in range(n):
        row = mat[i]
        print(" ".join(list(map(str, row))))