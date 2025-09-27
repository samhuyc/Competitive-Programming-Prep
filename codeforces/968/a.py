
import math
import heapq
import re
from collections import deque, defaultdict



t = int(input())


for _ in range(t):
    n = int(input())
    st = input()

    
    
    if st[0] == st[-1]:
        print('NO')
    else:
        print('YEs')