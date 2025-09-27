
import math
import heapq
import re
from collections import deque, defaultdict, Counter



t = int(input())


for _ in range(t):
    n = int(input())
    s = input()


    c = list(dict(Counter(s)).items())
    c.sort(key=lambda x:-x[1])

    ans = ["" for _ in range(c[0][1])]

    curr = 0
    for letter, f in c:
        for ind in range(f):
            ans[(curr+ind)%len(ans)] += letter
        curr = (curr+ind+1)%len(ans)
    
    res = "".join(ans)
    print(res)
