t = int(input())

for _ in range(t):
    n, ind = list(map(int, input().split()))
    cows = list(map(int, input().split()))
    my = cows[ind-1]
    pos = None
    for i in range(ind-1):
        if cows[i] > my:
            pos = i
            break
    
    if pos == None:
        ans = 0
        cows[0], cows[ind-1] = my, cows[0]
        for i in range(1,n):
            if cows[i] < my:
                ans += 1
            else:
                break
    else:
        ans = 0 if pos == 0 else 1
        cows[pos], cows[ind-1] = my, cows[pos]
        # print(cows)
        for i in range(pos+1, n):
            if cows[i] < my:
                ans += 1
            else:
                break

        ans2 = pos - 1
        ans = max(ans2, ans)
    
    print(ans)

        
    
