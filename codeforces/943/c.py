
from collections import deque

t = int(input())

for _ in range(t):
    al = int(input())
    xlst = list(map(int, input().split()))
    ans = deque()

    divided = 10**9
    divisor = None
    ans.append(divided)
    for x in xlst[::-1]:
        divisor = divided - x
        divided = divisor
        ans.appendleft(divided)
    
    print(" ".join(list(map(str, ans))))






