

from sys import stdin, stdout
import heapq
import re
import math
from collections import deque, defaultdict, Counter


t = int(input())


for _ in range(t):
    n = int(input())
    vals = list(map(int, input().split()))
    lst = []
    for i in range(0, len(vals), 2):
        lst.append(vals[i])
    print(max(lst))