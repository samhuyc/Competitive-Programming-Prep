
import math
from collections import deque, Counter, defaultdict
import heapq
import re


t = int(input())


for _ in range(t):
    n = int(input())
    vals = list(map(int, list(input())))
    o = 0
    z = 0
    curr = False

    for i in range(len(vals)):

        if vals[i] == 1:
            o += 1
            curr = False
        else:
            if curr == False:
                z += 1
                curr = True
    
    # print(o, z)
    if o > z:
        print("Yes")
    else:
        print("No")
            
