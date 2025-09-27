t = int(input())

for _ in range(t):
    n, k = list(map(int, input().split()))
    dist = 2*k
    lst = list(map(int, input().split()))
    vals = [0]
    curr = 0
    for v in lst:
        curr = curr^v
        vals.append(curr)
    # print(vals)
    dic = {}
    ans = (None, None)
    for i in range(dist, n+1):
        value = vals[i]^vals[i-dist]
        dic[value] = (i, i-dist+1)
        # print(dic)
    
    for j in range(n+dist, 2*n+1):
        value = vals[j]^vals[j-dist]
        if value in dic:
            ans = (dic[value], (j,j-dist+1))
    
    # print(ans)
    l = ans[0]
    r = ans[1]
    llst = lst[l[1]-1:l[0]]
    rlst = lst[r[1]-1:r[0]]
    print(' '.join(list(map(str, llst))))
    print(' '.join(list(map(str, rlst))))