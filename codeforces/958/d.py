
import math
from collections import deque, Counter, defaultdict
import heapq
import re


t = int(input())

def he(curr):
    
    visited[curr] = True

    neighbor = adjlist[curr]
    fneighbor = []
    first = 0
    for n in neighbor:
        if not visited[n]:
            fneighbor.append(n)

    second = attack[curr]
    sneighbor = []
    for f in fneighbor:
        for n in adjlist[f]:
            if not visited[n]:
                sneighbor.append(n)

    for f in fneighbor:
        first += he(f)
    for s in sneighbor:
        second += he(s)

    return max(first, second)

for _ in range(t):

    n = int(input())
    attack = list(map(int, input().split()))
    adjlist =[[] for _ in range(n)]
    visited = [False] * n
    used = [False]*n

    for _ in range(n-1):
        a, b = list(map(int, input().split()))
        adjlist[a-1].append(b-1)
        adjlist[b-1].append(a-1)
    
    print(sum(attack))
    print(he(0))
    print(visited)
    


    
    
        


