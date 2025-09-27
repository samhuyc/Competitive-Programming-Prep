
import math
from collections import deque, defaultdict
import heapq


t = int(input())


for _ in range(t):

    n, m, k = list(map(int, input().split()))
    mat = []

    for _ in range(n):
        row = list(map(int, input().split()))
        mat.append(row)
    
    bo = []
    for _ in range(n):
        row = list(map(int, list(input())))
        bo.append(row)
    
    total = 0
    for i in range(n):
        for j in range(m):
            if bo[i][j] == 0:
                total += mat[i][j]
            else:
                total -= mat[i][j]

    if total == 0:
        print("Yes")
        continue
    
    newbo = []
    for row in bo:
        curr = 0
        currrow = [0]
        for i in range(m):
            curr += 1 if row[i] == 0 else -1
            currrow.append(curr)
        
        prefix = []
        for i in range(k, m+1):
            prefix.append(currrow[i]-currrow[i-k])

        newbo.append(prefix)
        

    flag = False
    gcd = None
    for j in range(len(newbo[0])):
        currsum = 0
        for row in range(k):
            currsum += newbo[row][j]
        
        if currsum != 0:
            if gcd == None:
                gcd = currsum
            else:
                gcd = math.gcd(currsum, gcd)
        
        if n > k:
            for i in range(k, n):
                currsum += newbo[i][j] - newbo[i-k][j]
                if currsum != 0:
                    if gcd == None:
                        gcd = currsum
                    else:
                        gcd = math.gcd(gcd, currsum)
        
        if gcd == None:
            continue

        if total%gcd == 0:
            flag = True
            break
    
    if flag:
        print("Yes")
    else:
        print("No")
                




        

    
