
import math
from collections import deque, Counter, defaultdict
import heapq
import re


t = int(input())

for _ in range(t):

    n = int(input())
    attack = list(map(int, input().split()))
    attack = [(a, i) for i, a in enumerate(attack)]
    adjlist =[[] for _ in range(n)]

    for _ in range(n-1):
        a, b = list(map(int, input().split()))
        adjlist[a-1].append(b-1)
        adjlist[b-1].append(a-1)

    heapq.heapify(attack)
    
    