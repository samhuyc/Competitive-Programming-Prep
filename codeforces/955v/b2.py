
import math
from collections import deque, defaultdict
import heapq


t = int(input())


for _ in range(t):

    x, y , k = list(map(int, input().split()))

    while k > 0:
        operation = y - (x%y)
        if operation > k:
            x += k
            k = 0
            break
        else:
            x += operation
            while x % y == 0:
                x = x//y
            
            k -= operation

            if x == 1:
                break
    
    if k > 0:
        x = k%(y-1)+1
    
    print(x)