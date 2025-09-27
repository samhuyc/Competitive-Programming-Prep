


t = int(input())

for _ in range(t):
    n = int(input())
    vals = list(map(int, input().split()))
    vals = [(v, i) for i, v in enumerate(vals)]
    vals.sort()
    ans = 0

    for v, i in vals:
        add = 0
        if i%2 == 0:
            add = (n+1)//2
            ans = max(ans, v+add)
        else:
            add = n//2
            ans = max(ans, v + add)

    print(ans)
            


