


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

    flag = False
    for i, row in enumerate(mat):
        c = dict(Counter(row))
        d = dict(Counter(target[i]))

        for v in [0, 1,2]:
            if v not in c:
                c[v] = 0
            if v not in d:
                d[v] = 0
        
        print(c, d)
        if ((c[0]-d[0])%2 != 0) and ((c[1]-d[1])%2 != 0) and ((c[2]-d[2])%2 != 0):
            flag = True
            break
    

    Tmat = []
    for i in range(m):
        col = []
        for j in range(n):
            col.append(mat[j][i])
        Tmat.append(col)
    
    Ttarget = []
    for i in range(m):
        col = []
        for j in range(n):
            col.append(target[j][i])
        Ttarget.append(col)
    
    for i, row in enumerate(Tmat):
        c = dict(Counter(Tmat[i]))
        d = dict(Counter(Ttarget[i]))

        for v in [0, 1,2]:
            if v not in c:
                c[v] = 0
            if v not in d:
                d[v] = 0
        print(c, d)
        if ((c[0]-d[0])%2 != 0) and ((c[1]-d[1])%2 != 0) and ((c[2]-d[2])%2 != 0):
            flag = True
            break


    print(Tmat, Ttarget)
    if flag:
        print('No')
    else:
        print('Yes')


                



    
