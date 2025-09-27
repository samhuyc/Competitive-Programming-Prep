
import math
from collections import deque, Counter, defaultdict
import heapq
import re


t = int(input())


for _ in range(t):

    n = int(input())
    bi = bin(n)[2:]

    onepos = []
    for i, char in enumerate(bi):
        if char == "1":
            onepos.append(i)

    count = len(onepos)

    ma = int("1"*count,2)
    totlen = len(bi)


    curr = ma-1
    nxt = curr-1
    fillin = [ma, curr]
    while nxt > 0:
        if curr | nxt != ma:
            nxt -= 1
        else:
            fillin.append(nxt)
            curr = nxt
            nxt = curr - 1

    ans = []

    for f in fillin:
        if f <= 0:
            continue

        new = ["0"]*totlen
        bif = bin(f)[2:]
        bif = "0"*(count - len(bif)) + bif
        

        for i, p in enumerate(onepos):
            new[p] = bif[i]
        
        ans.append(int("".join(new), 2))
    
    ans = ans[::-1]
    print(len(ans))
    print(" ".join(list(map(str, ans))))

    
    
        



            
        
        