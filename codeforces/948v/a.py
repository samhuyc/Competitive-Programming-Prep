
import math
from collections import deque, defaultdict, Counter
import heapq




t = int(input())


for _ in range(t):


    n, m = list(map(int, input().split()))
    if m > n:
        print("No")
    elif m%2 != n%2:
        print("No")
    else:
        print("Yes")
    
    