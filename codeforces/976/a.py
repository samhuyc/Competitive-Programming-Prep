
import math
import heapq
from collections import deque, defaultdict, Counter


t = int(input())



for _ in range(t):

    n, k = list(map(int, input().split()))
    if k == 1:
        print(n)
        continue

    ans = 0
    while n != 0 and math.floor(math.log(n, k)) >= 1:
        n -= k**math.floor(math.log(n, k))
        ans += 1
    
    ans += n
    print(ans)