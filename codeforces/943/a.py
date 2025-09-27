
import math

t = int(input())


for _ in range(t):
    x = int(input())
    ans = None
    curr = 0

    for y in range(1, x):
        now = math.gcd(x,y)+y
        if now > curr:
            ans = y
            curr = now
    
    print(ans)