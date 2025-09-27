
from collections import deque
import math
import heapq

t = int(input())


for _ in range(t):
    n = int(input())
    adjlst = [[] for _ in range(n)]
    degree = [0] * n

    for _ in range(n-1):
        a, b = list(map(int, input().split()))
        a = a-1
        b = b-1
        adjlst[a].append(b)
        adjlst[b].append(a)
        degree[a] += 1
        degree[b] += 1
    
    depth = [None] * n
    tovisit = deque()
    tovisit.append((0,0))

    while tovisit:
        curr, currdepth = tovisit.popleft()
        if depth[curr] != None:
            continue
        depth[curr] = currdepth
        neighbors = adjlst[curr]
        sent = False
        for n in neighbors:
            tovisit.append((n, currdepth+1))


    print(degree)


    minleaves = []
    maxleaves = []
    mindepth = math.inf
    maxdepth = 0
    for i in range(n):
        if degree[i] == 1:
            heapq.heappush(minleaves, (-depth[i], i))
            heapq.heappush(maxleaves, (depth[i], i))
            maxdepth = max(maxdepth, depth[i])
            mindepth = min(mindepth, depth[i])
        else:
            print(i)
    
    print(minleaves, maxleaves)
    ans = math.inf

    for target in range(maxdepth, mindepth-1, -1):
        currmin = minleaves.copy()
        currmax = maxleaves.copy()
        degree = degree.copy()
        
        time = 1
        res = 0
        good = [False, False]
        while True:
            print(currmin, currmax)
            if time == 1:
                good[time] = True
                while currmin and -currmin[0][0] > target:
                    res += 1
                    good[time] = False
                    _, node = heapq.heappop(currmin)
                    for n in adjlst[node]:
                        degree[n] -= 1
                        if degree[n] == 1:
                            heapq.heappush(currmin, (-depth[n], n))
                            heapq.heappush(currmax, (depth[n], n))
                
                if all(good):
                    break
                else:
                    time = 0
            
            else:
                good[time] = True
                while currmax and currmax[0][0] < target:
                    res += 1
                    good[time] = False
                    _, node = heapq.heappop(currmax)
                    for n in adjlst[node]:
                        degree[n] -= 1
                        if degree[n] == 1:
                            heapq.heappush(currmin, (-depth[n], n))
                            heapq.heappush(currmax, (depth[n], n))
                
                if all(good):
                    break
                else:
                    time = 1

        ans = min(ans, res)
    
    print(ans)





