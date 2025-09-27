


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
    lim = tot//3
    # print(lim)

    a, b, c = 0, 0, 0
    al, ar, bl, br, cl, cr = None, None, None, None, None, None
    ind = 0
    fail = False
    finished = False

    # print(alst, blst, clst)
    
    while True:
        a += alst[ind]
        b += blst[ind]
        c += clst[ind]
        print(a, b, c, ind, lim)

        if a >= lim:
            # print('here')
            al, ar = 0, ind
            b = 0
            c = 0
            ind2 = ind+ 1
            while True:
                b += blst[ind2]
                c += clst[ind2]
                print(b, c, ind2)
                if b >= lim:
                    bl, br = ind+1, ind2
                    cl, cr = ind2 + 1, n-1
                    finished = True
                    print('here', ind2)
                    break
                elif c >= lim:
                    cl, cr = ind+1, ind2
                    bl, br = ind2 + 1, n-1
                    finsihed = True
                    break
                

                ind2 += 1
                if ind2 >= n:
                    fail = True
                    break

        elif b >= lim:
            bl, br = 0, ind
            a = 0
            c = 0
            ind2 = ind+ 1
            while True:
                a += alst[ind2]
                c += clst[ind2]
                if a >= lim:
                    al, ar = ind+1, ind2
                    cl, cr = ind2 + 1, n-1
                    finished = True
                    break

                elif c >= lim:
                    cl, cr = ind+1, ind2
                    al, ar = ind2 + 1, n-1
                    finished = True
                    break

                ind2 += 1
                if ind2 >= n:
                    fail = True
                    break

        elif c >= lim:
            cl, cr = 0, ind
            a = 0
            b = 0
            ind2 = ind+ 1
            while True:
                a += alst[ind2]
                b += blst[ind2]
                if a >= lim:
                    al, ar = ind+1, ind2
                    bl, br = ind2 + 1, n-1
                    finished = True
                    break
                elif b >= lim:
                    bl, br = ind+1, ind2
                    al, ar = ind2 + 1, n-1
                    finished = True
                    break
                else:
                    ind2 += 1
                    if ind2 >= n:
                        fail = True
                        break
        
        if finished:
            break

        ind += 1
        if ind >= n:
            fail = True
            break

        elif fail:
            break

    
    if fail:
        print(-1)
    else:
        if sum(alst[al:ar+1]) > lim and sum(blst[bl:br+1]) > lim and sum(clst[cl:cr+1])>lim:
            
            print(al, ar, bl, br, cl, cr)
        else:
            print(al, ar, bl, br, cl, cr)
            print(lim)
            print(-1)
    

        
        
