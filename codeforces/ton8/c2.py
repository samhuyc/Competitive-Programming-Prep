

t = int(input())
for _ in range(t):
    n, x, y = list(map(int, input().split()))
    xlst = list(map(int, input().split()))
    xlst.sort()
    ans = x+y-2

    diff = []

    for i in range(len(xlst)-1):
        if (xlst[i+1] - xlst[i]) == 1:
            continue
        elif (xlst[i+1] - xlst[i]) == 2:
            ans += 1
        else:
            diff.append(xlst[i+1] - xlst[i])

    if (xlst[0]- xlst[-1]) + n == 2:
        ans += 1
    elif (xlst[0]- xlst[-1]) + n != 1:
        diff.append((xlst[0]- xlst[-1]) + n)
    

    diff.sort(key = lambda x:(x%2, x))
    ind = 0
    while ind< len(diff) and y > 0:
        d = diff[ind]
        use = min((d-1)//2, y)
        y -= use
        ans += use + 1 if 2*use +2 == d else use
        ind += 1


    print(min(n-2, ans))
