t = int(input())

for _ in range(t):
    n, k = list(map(int, input().split()))
    stalls = []
    
    pow = 0
    while True:
        curr = 2**pow - 1
        remain = n - curr
        if remain/(curr+1)+curr >= k:
            

        


    
