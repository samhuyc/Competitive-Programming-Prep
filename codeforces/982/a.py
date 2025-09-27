

import math
from collections import deque, defaultdict, Counter



t = int(input())


for _ in range(t):
    n = int(input())
    stamps = [list(map(int, input().split())) for _ in range(n)]

    mat = [0 for _ in range(200)]
    for x, y in stamps:
        for i in range(x):
            mat[i] = max(mat[i], y)
    
    ans = 0
    for i in mat:
        if i == 0:
            break
        else:
            ans += 2
    
    ans += max(mat)*2
    
    # print(mat[:10])
    print(ans)


