
import math


t = int(input())


for _ in range(t):
    n, m = list(map(int, input().split()))
    info = []
    lookup = {'n':0,'a':1,'r':2,'e':3,'k':4}
    dp = [-math.inf for _ in range(5)]
    dp[0] = 0

    for stringind in range(n):
        line = list(input())
        info = [lookup[char] for char in line if char in lookup]

        newdp = [v for v in dp]

        for j in range(5):
            if dp[j] < 0:
                continue
            
            score = 0
            nxt = j

            for char in info:
                if char == nxt:
                    nxt = (nxt+1)%5
                    score += 1
                else:
                    score -= 1
            
            newdp[nxt] = max(newdp[nxt], dp[j]+score)
        dp = newdp
    
    ans = 0 
    for i in range(5):
        ans = max(ans, dp[i]-i*2)
    print(ans)
            
            