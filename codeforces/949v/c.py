

import math
from collections import deque
 
t = int(input())
 
 
for _ in range(t):
    n = int(input())
    ap = list(map(int, input().split()))
    
    counter = 0
    vpiece = []
    valslst = []
    freqlst = []
    for v in ap:
        if v == -1:
            counter += 1
            if vpiece:
                valslst.append(vpiece)
                vpiece = []
        else:
            vpiece.append(bin(v)[2:])
            freqlst.append(counter)
            counter = 0
    freqlst.append(counter)
    if vpiece:
        valslst.append(vpiece)


    ans = []
    if valslst == []:
        ans = [i%2+1 for i in range(freqlst[0])]
        print(" ".join(map(str, ans)))
        continue
    
    warn = False
    for vpiece in valslst:
        for i in range(len(vpiece)-1):
            l, r = int("0b"+vpiece[i], base=0), int("0b"+vpiece[i+1], base=0)
            if l//2 != r and r//2 != l:
                warn = True
                break
        if warn == True:
            break
    if warn:
        print(-1)
        continue



    headlst = deque()
    if freqlst[0] != 0:
        head = int("0b"+valslst[0][0], base=0)
        if head != 1:
            for i in range(freqlst[0]):
                if i % 2 == 0:
                    headlst.appendleft(head//2) 
                else:
                    headlst.appendleft(head)
        else:
            for i in range(freqlst[0]):
                if i % 2 == 0:
                    headlst.appendleft(head*2) 
                else:
                    headlst.appendleft(head)
    
    tailst = deque()
    if freqlst[-1] != 0:
        tail = int("0b"+valslst[-1][-1], base = 0)
        if tail != 1:
            for i in range(freqlst[-1]):
                if i % 2 == 0:
                    tailst.append(tail//2) 
                else:
                    tailst.append(tail)
        else:
            for i in range(freqlst[-1]):
                if i % 2 == 0:
                    tailst.append(tail*2) 
                else:
                    tailst.append(tail)


    flag = False
    pieces = []

    for i in range(len(valslst)-1):
        l, r = valslst[i][-1], valslst[i+1][0]
        block = freqlst[i+1]
        change = block + 1
        same = 0
        for j in range(min(len(l), len(r))):
            if l[j] == r[j]:
                same += 1
            else:
                break
        diff = len(l) + len(r) - 2*same

        if change %2 != diff %2:
            flag = True
            break
        elif change < diff:
            flag = True
            break
        else:
            piece = []
            curr = l
            finished = False
            for i in range(block):
                if not finished and len(curr) > same:
                    curr = curr[:-1]
                elif not finished and len(curr) == same:
                    finished = True

                if finished:
                    if len(curr) >= len(r):
                        if len(curr) > 1:
                            curr = curr[:-1]
                        else:
                            curr = curr + "0"
                    else:
                        curr += r[len(curr)]
                piece.append(curr)
            pieces.append(piece)



    if flag == True:
        print(-1)
    else:
        res = []
        if headlst:
            res.extend(headlst)
        if pieces:
            for i, p in enumerate(pieces):
                for v in valslst[i]:
                    res.append(int("0b"+v, base=0))
                for v in p:
                    res.append(int("0b"+v, base=0))
        for v in valslst[-1]:
            res.append(int("0b"+v, base=0))
        if tailst:
            res.extend(tailst)
        print(" ".join(map(str, res)))

    # print(valslst)
    # print(freqlst)
    # print(headlst, pieces, tailst)


        