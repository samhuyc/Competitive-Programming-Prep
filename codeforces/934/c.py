import heapq
from collections import Counter

t = int(input())

for _ in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    c = list(dict(Counter(lst)).items())
    c.sort()
    
    prev = -1
    ans = None
    first = None
    second = None
    
    # print(c)
    for v, f in c:
        if v > prev+1:
            ans = prev +1
            break
        if f == 1 and first == None:
            first = True
        elif f == 1 and first != None:
            ans = v
            break
        prev = v

    if ans == None:
        ans = c[-1][0]+1
        print(ans)
    else:
        print(ans)