

import heapq
import math
from collections import deque, defaultdict


t = int(input())

for _ in range(t):

    word1, word2 = input().split()
    ans1 = word2[0] + word1[1:]
    ans2 = word1[0] + word2[1:]
    print(ans1 + " " + ans2)