import math

t = int(input())
for _ in range(t):
    n = int(input())
    curr = 1
    while curr <= n:
        curr *= 2
    
    print(curr//2)
    


