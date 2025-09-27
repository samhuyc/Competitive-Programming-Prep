t = int(input())

for _ in range(t):
    n, m = list(map(int, input().split()))
    n = n%m


    if n == 0:
        print(0)
        continue
    elif m % 2 != 0:
        print(-1)
        continue

    curr = 0
    good = {}

    while curr % 2 == 0:
        curr = int((curr+m)/2)
        good[curr] = True
    good[0] = True
    

    if (n not in good):
        print(-1)
    else:
        ans = n
        while n != 0:
            n = (n*2)%m
            ans += n
        
        print(ans)





