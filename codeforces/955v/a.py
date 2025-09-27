
import math
from collections import deque, defaultdict
import heapq


t = int(input())


for _ in range(t):

    a, b = list(map(int, input().split()))
    c, d = list(map(int, input().split()))

    if a > b and c < d:
        print("No")
    elif b > a and d < c:
        print("No")
    else:
        print("Yes")

