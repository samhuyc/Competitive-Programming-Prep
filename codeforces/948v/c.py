import math
from collections import deque, defaultdict, Counter
from functools import reduce


t = int(input())


for _ in range(t):

    n = int(input())
    lst = list(map(int, input().split()))
    lst.sort(reverse=True)

    dic = {}
    for v in lst:
        dic[v] = True

    mat =[[None] * n for _ in range(n)]
    ans = 0
    for i in range(n):
        cant = [lst[i]]
        for j in range(i, n):
            up, down = lst[i], lst[j]
            if up % down != 0:
                cant.append(down)
        lcm = reduce(math.lcm, cant)
        if lcm in dic:
            continue
        else:
            ans = n-i
            break
    
    print(ans)


            




