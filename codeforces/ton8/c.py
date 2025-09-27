

t = int(input())
for _ in range(t):
    n, x, y = list(map(int, input().split()))
    xlst = list(map(int, input().split()))
    xlst.sort()
    ans = x-2
    for i in range(len(xlst)-1):
        if (xlst[i+1] - xlst[i]) == 2:
            ans += 1
    if (xlst[0]- xlst[-1]) + n == 2:
        ans += 1
    print(ans)
