t = int(input())

for _ in range(t):
    n, m, k = list(map(int, input().split()))
    prices = list(map(int, input().split()))
    lst = [(v, i) for i, v in enumerate(prices)]
    lst.sort(key=lambda x:(x[0],-x[1]))
    info = []
    
    for p, ind in lst:
        delta = min(k, m)
        info.append((p, ind, delta))
        k -= delta
        if k == 0:
            break
    
    info.sort(key = lambda x:x[1])
    # print(info)

    sum = 0
    ans = 0
    for p, ind, delta in info:
        ans += (p+sum)*delta
        sum += delta
    
    print(ans)