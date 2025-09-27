

import math
from collections import deque, defaultdict, Counter



t = int(input())


for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    alst = [[v-(n-i), i] for i, v in enumerate(a)]
    alst.sort()
    
    tovisit = deque([])
    for curr, delta in alst:
        if curr == 0:
            tovisit.append((curr, delta, 0))
    
    dic = {}
    for curr, delta in alst:
        if curr in dic:
            dic[curr].append(delta)
        else:
            dic[curr] = [delta]


    ans = 0
    visited = {}

    while tovisit:
        curr, delta, leng = tovisit.popleft()
        ans = max(ans, curr+delta)
        if curr+delta in visited:
            continue
        else:
            visited[curr+delta] = True

        if curr + delta in dic:
            nxt = dic[curr+delta]
            for neighbor in nxt:
                tovisit.append((curr+delta, neighbor, leng+delta))
    
    print(n+ans)