


import math
from collections import deque, defaultdict
import heapq


t = int(input())

for _ in range(t):

    n = int(input())
    alst = list(map(int, input().split()))
    blst = list(map(int, input().split()))
    clst = list(map(int, input().split()))

    tot = sum(alst)
    lim = tot//3 if tot%3 == 0 else math.ceil(tot/3)

    a, b, c = 0, 0, 0
    al, ar, bl, br, cl, cr = None, None, None, None, None, None

    asu = []
    bsu = []
    csu = []

    for i in range(n):
        a += alst[i]
        b += blst[i]
        c += clst[i]
        asu.append(a)
        bsu.append(b)
        csu.append(c)

    # print(asu, bsu, csu)

    avis, bvis, cvis = False, False, False
    finished = False

    for i in range(n):
        if asu[i] >= lim and not avis:
            al, ar = 0, i
            avis = True
            finished = False
            for j in range(i+1, n-1):
                if (bsu[j]-bsu[i]) >= lim and (csu[-1]-csu[j])>=lim:
                    bl, br = i+1, j
                    cl, cr = j+1, n-1
                    finished = True
                    break
                elif (csu[j]-csu[i]) >= lim and (bsu[-1]-bsu[j])>=lim:
                    cl, cr = i+1, j
                    bl, br = j+1, n-1
                    finished = True
                    break


        elif bsu[i] >= lim and not bvis:
            bl, br = 0, i
            bvis = True
            finished = False
            for j in range(i+1, n-1):
                if (asu[j]-asu[i]) >= lim and (csu[-1]-csu[j])>=lim:
                    al, ar = i+1, j
                    cl, cr = j+1, n-1
                    finished = True
                    break
                elif (csu[j]-csu[i]) >= lim and (asu[-1]-asu[j])>=lim:
                    cl, cr = i+1, j
                    al, ar = j+1, n-1
                    finished = True
                    break


        
        elif csu[i] >= lim and not cvis:
            cl, cr = 0, i
            cvis = True
            finished = False
            for j in range(i+1, n-1):
                if (bsu[j]-bsu[i]) >= lim and (asu[-1]-asu[j])>=lim:
                    bl, br = i+1, j
                    al, ar = j+1, n-1
                    finished = True
                    break
                elif (asu[j]-asu[i]) >= lim and (bsu[-1]-bsu[j])>=lim:
                    al, ar = i+1, j
                    bl, br = j+1, n-1
                    finished = True
                    break


        if finished:
            break

    if not finished:
        print(-1)
    else:
        print(al+1, ar+1, bl+1, br+1, cl+1, cr+1)




