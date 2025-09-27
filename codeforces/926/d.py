t = int(input())
from collections import deque

for _ in range(t):
    n = int(input())
    edges = [[] for _ in range(n)]
    connect = [0 for _ in range(n)]
    visited = [0 for _ in range(n)]
    for _ in range(n-1):
        l, r = list(map(int, input().split()))
        l -= 1
        r -= 1
        connect[l] += 1
        connect[r] += 1
        edges[l].append(r)
        edges[r].append(l)
    
    tovisit = deque()
    for node, val in enumerate(connect):
        if val == 1:
            tovisit.append(node)
    
    ans = []

    while tovisit:
        curr = tovisit.popleft()
        if visited[curr] != 0:
            continue
        visited[curr] = 1
        
        temp = len(tovisit)
        # ans.append(len(tovisit))

        for val in edges[curr]:
            connect[val] -= 1
            if connect[val] == 1 and visited[val] == 0:
                tovisit.append(val)
        ans.append(min(temp, len(tovisit)))
        # print(curr)
        # print(tovisit)
        # ans.append(len(tovisit))
    print(ans)
    


    
    