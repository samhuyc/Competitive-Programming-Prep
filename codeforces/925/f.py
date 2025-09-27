from collections import deque

t = int(input())

for _ in range(t):
    n, k = list(map(int, input().split()))
    edges = [[] for _ in range(n+1)]
    start = {}
    for _ in range(k):
        lst = list(map(int, input().split()))
        for ind in range(2, n):
            if ind == 2:
                start[lst[ind]] = True
            v = lst[ind]
            prev = lst[ind-1]
            edges[v].append(prev)
    
    bad = 0
    visited = [0 for _ in range(n+1)]
    for s,_ in start.items():
        if visited[s] == 0:
            tovisit = deque()
            tovisit.append((s, -1))
            while tovisit:
                curr, prev = tovisit.popleft()
                if visited[curr] != 0:
                    continue
                else:
                    visited[curr] = 1

                if prev == -1:
                    for neighbors in edges[curr]:
                        tovisit.append((neighbors, curr))
                else:
                    for neighbors in edges[curr]:
                        if visited[neighbors] != 0:
                            bad = 1
                            break

                        tovisit.append((neighbors, curr))
                
                if bad == 1:
                    break
            if bad == 1:
                break

    if bad == 1:
        print('NO')
    else:
        print('YES')
    

    