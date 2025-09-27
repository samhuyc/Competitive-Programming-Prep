
import math
from collections import deque, defaultdict
import heapq


t = int(input())


for _ in range(t):

    n, mi, ma = list(map(int, input().split()))
    cards = list(map(int, input().split()))

    cards = deque(cards)
    ans = 0
    sum = 0
    l, r = 0, 0

    while r < n:
        nxt = cards[r]
        sum += nxt

        if mi <= sum <= ma:
            ans += 1
            r += 1
            l = r
            sum = 0
        elif sum < mi:
            r += 1
        else:
            while l <= r and sum > ma:
                sum -= cards[l]
                l += 1
            if mi <= sum <= ma:
                r += 1
                l = r
                sum = 0
                ans += 1
            else:
                r += 1
    print(ans)


                


