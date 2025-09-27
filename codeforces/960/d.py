


from sys import stdout
from collections import deque, defaultdict, Counter
import heapq
import re
import math


t = int(input())

for _ in range(t):
    n = int(input())
    lst = list(map(int, input().split()))

    ans = n
    vals = ""

    for i, v in enumerate(lst):
        if v == 0:
            ans -= 1
            vals += "0"
        elif v > 4:
            vals += "0"
        elif v <= 2:
            vals += "2"
        else:
            vals += "4"

    lst= vals.split("2")
    i = 1
    while i < len(lst)-1:
        if '0' not in lst[i] and len(lst[i])%2 == 0:
            ans -= 1
            i += 1
        i += 1
        

    print(ans)







    