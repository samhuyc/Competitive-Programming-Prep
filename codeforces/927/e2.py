t = int(input())
 
for _ in range(t):
    n = int(input())
    val = list(map(int, list(input())))
    base = 1
    ans2 = 0
    for ind in range(-1,-n-1,-1):
        v = val[ind]
        ans2 += base*v
        base = base * 10+1
    print(ans2)