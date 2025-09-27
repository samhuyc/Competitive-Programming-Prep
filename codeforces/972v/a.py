

from collections import deque, defaultdict
import heapq
import re
import math



t = int(input())

for _ in range(t):
    n = int(input())

    letters = ["a",'e','i','o','u']
    vals = ""

    if n <= 5:
        print("".join(letters[:n]))
        continue
    else:
        mult = n//5
        remain = n%5
        for i in range(5):
            if i < remain:
                vals += letters[i]*(mult+1)
            else:
                vals+= letters[i]*(mult)
        print(vals)
        continue
