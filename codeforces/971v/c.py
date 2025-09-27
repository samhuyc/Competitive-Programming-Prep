
from collections import defaultdict, deque, Counter
import math



t = int(input())


for _ in range(t):
    x, y, d = list(map(int, input().split()))

    a, b = math.ceil(x/d), math.ceil(y/d)

    if a > b:
        print(max(a, b)*2-1)
    else:
        print(max(a, b)*2)