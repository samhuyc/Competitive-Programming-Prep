t = int(input())

for _ in range(t):
    nlen, mlen, k = list(map(int, input().split()))
    n = list(set(list(map(int, input().split()))))
    m = list(set(list(map(int, input().split()))))
    nval = [0 for _ in range(k)]
    mval = [0 for _ in range(k)]

    for val in n:
        curr = val -1
        if curr >= k:
            continue
        else:
            nval[curr] = 1
    
    for val in m:
        curr = val -1
        if curr >= k:
            continue
        else:
            mval[curr] = 1      

    ans = 1
    ncount = 0
    mcount = 0

    for i in range(k):
        if nval[i] == 0 and mval[i] == 0:
            ans = 0
            break
        if nval[i] == 1 and mval[i] == 0:
            ncount += 1
            if ncount > k//2:
                ans = 0
                break
        elif nval[i] == 0 and mval[i] == 1:
            mcount += 1
            if mcount > k//2:
                ans = 0
                break

    
    if ans:
        print('YES')
    else:
        print('NO')
