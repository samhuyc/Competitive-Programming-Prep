t = int(input())


for _ in range(t):
    n, k = list(map(int, input().split()))
    ans = n
    reduction = n-1

    if k >= n*(n-1)/2:
        print(1)
        continue

    while k - reduction >= 0:
        k -= reduction
        reduction -= 1
        ans -= 1
        # print(ans)
        
    
    print(ans)