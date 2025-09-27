import math


t = int(input())

for _ in range(t):
    n = int(input())
    base = 1
    ans = 0
    sn = str(n)

    for i in range(-1, -len(sn)-1, -1):
        curr = int(sn[i])
        
        
        if i > -len(sn):
            prev = int(sn[:i])
            ans += prev*45*(10**(-i-1))

        if i != -1:
            if curr >= 1:
                ans += ((curr-1)*curr//2)*(10**(-i-1))
            ans += curr * (int(sn[i+1:])+1)

        else:
            ans += ((curr)*(curr+1)//2)

    print(ans)
        
        
    
    