

import heapq
import math
from collections import deque, defaultdict


t = int(input())

for _ in range(t):

    n = int(input())
    vals = list(map(int, input().split()))

    visited = dict()
    sum = 0
    ans = 0

    for i in range(n):
        new = vals[i]

        if sum == new:
            ans += 1
        else:
            if (sum + new) % 2 == 0:
                target = (sum + new)//2
                if target in visited:
                    ans += 1
        visited[new] = True
        sum += new
    print(ans)
                    

                



