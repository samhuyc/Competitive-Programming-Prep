


from collections import deque, defaultdict
import heapq
import math



t = int(input())

for _ in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    ans = max(lst)
    for i in range(len(lst)-1):
        l, r = lst[i], lst[i+1]
        currma = max(l,r)
        ans = min(currma-1, ans)
    print(ans)
    