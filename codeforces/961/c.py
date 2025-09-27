

from sys import stdin, stdout
import math
import re
import heapq
from collections import deque, Counter, defaultdict


t = int(input())

for _ in range(t):

    n = int(input())
    vals = list(map(int, input().split()))

    ans = 0

    flag = True

    for i in range(1, n):
        while vals[i] < vals[i-1]:
            if vals[i] == 1:
                flag = False
                break
            need = math.ceil(math.log(math.log(vals[i-1], vals[i]), 2))
            # print(vals[i], vals[i-1], need)
            ans += need
            vals[i] = vals[i] ** (2**need)

        if flag == False:
            break
    
    if not flag:
        print(-1)
    else:
        print(ans)
    
    