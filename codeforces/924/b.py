t = int(input())

for _ in range(t):
    k = int(input())
    lst = list(map(int, input().split()))
    lst.sort()
    vals = [lst[0]]

    for v in lst:
        if v != vals[-1]:
            vals.append(v)

    
    l = 0
    r = 0
    n = len(vals)
    ans = 1
    while r<n:
        if vals[r] - vals[l] <= k-1:
            r += 1
            ans = max(ans, r-l)
        else:
            l += 1
            if l == r:
                r += 1
    
    print(ans)


