t = int(input())

for _ in range(t):
    n = int(input())
    years = list(map(int, input().split()))
    ans = 0
    for y in years:
        ans += 1
        if ans//y == 0:
            ans = y
        elif ans % y != 0:
            ans = (ans//y)*y + y
    
    print(ans)