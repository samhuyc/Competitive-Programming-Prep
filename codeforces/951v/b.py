
from collections import deque, defaultdict
import heapq
import math



t = int(input())

for _ in range(t):
    x, y = list(map(int, input().split()))

    xbin = bin(x)[2:]
    ybin = bin(y)[2:]
    malen = max(len(xbin), len(ybin))
    xbin = "0"*(malen-len(xbin)) + xbin
    ybin = "0"*(malen-len(ybin)) + ybin

    ans = 0
    flag = True
    for i in range(-1, -len(xbin), -1):
        if xbin[i] == ybin[i]:
            ans += 1
        else:
            break

    print(2**ans)
