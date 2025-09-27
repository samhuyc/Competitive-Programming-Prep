
import math
from collections import deque, defaultdict
import heapq


t = int(input())


for _ in range(t):

    x, y , k = list(map(int, input().split()))

    power = int(math.log(x, y))
    
    bi = []

    while x > 0:
        digit = x//(y**power)
        bi.append(digit)
        x = x % (y**power)
        power -= 1

    bi = deque(reversed(bi))

    while k > 0:
        if bi:
            curr = y - bi.popleft()
            




