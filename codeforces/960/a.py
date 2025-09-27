


from sys import stdout
from collections import deque, defaultdict, Counter
import heapq
import re
import math


t = int(input())

for _ in range(t):
    n = int(input())
    vals = list(map(int, input().split()))

    c = list(dict(Counter(vals)).items())

    c.sort(key=lambda x:-x[0])
    flag = False
    for v, f in c:
        if f%2 == 1:
            flag = True
    
    if flag:
        print('YES')
    else:
        print('No')


