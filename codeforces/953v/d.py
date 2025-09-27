

import heapq
from collections import defaultdict, deque
import math



t = int(input())

for _ in range(t):

    n, c = list(map(int, input().split()))
    fans = list(map(int, input().split()))

    ans = [None] * n

    undecided = c
    currtop = 0
    currelim = 0

    lst = [(fans[i], i) for i in range(n)]
    lst.sort(reverse=True, key = lambda x:(x[0], -x[1]))

    i = 0

    while i < n:

        while currtop < n and ans[currtop] != None:
            currtop += 1

        if ans[i] != None:
            i += 1
            continue

        front = fans[currtop] + undecided
        best, bestind = lst[i]

        # print(front, currtop)
        # print(best, bestind)

        if best > front:
            ans[bestind] = currelim
            undecided += best
            currelim += 1
        else:
            ans[currtop] = currelim
            undecided += fans[currtop]
            currelim += 1

    prefix = []
    carry = c
    heap = []
    for val, ind in lst:
        heapq.heappush(heap, (-val, ind))

    visited = [False] * n
    for i, f in enumerate(fans):
        while heap and heap[0][1] <= i:
            heapq.heappop(heap)
        
        if not heap:
            break

        if f + carry >= -heap[0][0]:
            ans[i] = min(ans[i], i)
        
        carry += f
        
    print(" ".join(list(map(str, ans))))
        
    # print(ans)



        









