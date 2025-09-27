
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

    ans = []
    for i in range(count):
        new = ["0"] * totlen
        for j, p in enumerate(onepos):
            if j != i:
                new[p] = "1"
        v = int("".join(new),2)
        if v > 0:
            ans.append(v)
    
    ans.append(n)
    print(len(ans))
    print(" ".join(list(map(str, ans))))
        
