


import math
from collections import deque, defaultdict, Counter
import heapq


t = int(input())

for _ in range(t):

    n, m = list(map(int, input().split()))
    mat = []
    for _ in range(n):
        row = list(map(int, list(input())))
        mat.append(row)

    target = []
    for _ in range(n):
        row = list(map(int, list(input())))
        target.append(row)

    flag = True
    for y in range(n):
        if not flag:
            break
        for x in range(m):
            curr, tarcurr = mat[y][x], target[y][x]
            if curr == tarcurr:
                continue
            else:
                diff = (tarcurr - curr)%3
                if y == n-1 or x == m-1:
                    flag = False
                    break
                mat[y][x] = tarcurr
                if diff == 1:
                    mat[y][x+1] = (mat[y][x+1]+2)%3
                    mat[y+1][x] = (mat[y+1][x]+2)%3
                    mat[y+1][x+1] = (mat[y+1][x+1]+1)%3
                else:
                    mat[y][x+1] = (mat[y][x+1]+1)%3
                    mat[y+1][x] = (mat[y+1][x]+1)%3
                    mat[y+1][x+1] = (mat[y+1][x+1]+2)%3
            
            # for line in mat:
            #     print(line)
            #     print("***")
    
    if flag:
        print('Yes')
    else:
        print('No')


