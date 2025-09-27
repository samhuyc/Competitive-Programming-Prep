from collections import deque
import heapq


t = int(input())

for _ in range(t):
    n, k = list(map(int, input().split()))
    mat = []
    for _ in range(n):
        info = list(map(int, input().split()))
        add = [None] * (n-len(info))
        info = add + info
        mat.append(info)
    
    hp = []
    heapq.heappush(0)

    
    
    