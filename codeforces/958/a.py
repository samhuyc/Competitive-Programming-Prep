
import math
from collections import deque, Counter, defaultdict
import heapq
import re


t = int(input())


for _ in range(t):

    n, k = list(map(int, input().split()))
    
    if n == 1:
        print(0)
        continue
    
    if (n-1)%(k-1) == 0:
        print((n-1)//(k-1))
    else:
        print((n-1)//(k-1)+1)
