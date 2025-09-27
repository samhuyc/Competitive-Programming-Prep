t = int(input())

for _ in range(t):
    n = int(input())
    lst = list(map(int, input().split()))

    lst.sort()
    ans = 0
    for i in range(0, 2*n, 2):
        ans += lst[i]
    print(ans)