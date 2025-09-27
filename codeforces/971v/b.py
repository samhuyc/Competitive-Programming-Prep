

from collections import defaultdict, deque, Counter
import math



t = int(input())


for _ in range(t):
    n = int(input())
    val = []
    for _ in range(n):
        row = list(input())
        re = row.index("#")
        val.append(re+1)
    
    val = val[::-1]
    print(" ".join(list(map(str, val))))

    