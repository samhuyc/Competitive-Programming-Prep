

import heapq
from collections import defaultdict, deque
import math



t = int(input())

for _ in range(t):
    n, k = list(map(int, input().split()))
    if k % 2 != 0:
        print('No')
        continue

    tofill = [None] *( n+1)
    curr = k
    for i in range(1, n//2+1):
        opposite = n-i+1
        add = abs(opposite-i)
        if add * 2 <= curr:
            tofill[i] = opposite
            tofill[opposite] = i
            curr -= add*2
        else:
            need = curr//2 + i
            tofill[i] = need
            tofill[need] = i
            curr = 0
            break
    
    # print(tofill)
    if curr > 0:
        print('No')
        continue
    
    else:
        ans = []
        for i in range(1, n+1):
            if tofill[i] == None:
                ans.append(i)
            else:
                ans.append(tofill[i])
        print('Yes')
        print(" ".join(list(map(str, ans))))






