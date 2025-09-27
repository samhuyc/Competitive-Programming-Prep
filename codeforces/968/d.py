
import math
import heapq
import re
from collections import deque, defaultdict



t = int(input())


for _ in range(t):
    n, m = list(map(int, input().split()))
    vals = []
    for _ in range(n):
        line = list(map(int, input().split()))[1:]
        line = list(set(line))
        line.sort()
        ind = 0
        res = []
        for i in range(len(line)+2):
            if ind >= len(line):
                res.append(i)
            else:    
                if line[ind] == i:
                    ind += 1
                elif line[ind] > i:
                    res.append(i)
                else:
                    ind += 1
            if len(res) >= 2:
                break
        
        vals.append(res)

    mma = 0
    for x, y in vals:
        mma = max(mma, x, y)

    point = [None] * (mma + 5)
    vals.sort(key=lambda x:(-x[1], -x[0]))
    for start, result in vals:
        if point[start] == None:
            final_result = result
            while point[final_result] != None:
                final_result = point[final_result]
            point[start] = final_result

        else:
            final_prev = point[start]
            while point[final_prev] != None:
                final_prev = point[final_prev]
            
            prev = max(final_prev, result)
            
            for i in range(prev):
                if point[i] != None:
                    point[i] = max(point[i], prev)
                else:
                    point[i] = prev
            break

    ans = 0
    for i in range(len(point)):
        if point[i] == None:
            point[i] = i
        else:
            point[i] = max(point[i], i)
        ans += point[i]
    
    finished = len(point)
    ans += (len(point) + m) * (m-len(point)+1) //2
    print(ans)
    # print(point[:20])