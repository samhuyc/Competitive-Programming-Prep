t = int(input())

for _ in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    curr = 0
    flag = False

    while curr < n-2:
        if lst[curr] < 0:
            flag = True
            break
        lst[curr+1] -= lst[curr]*2
        lst[curr+2] -= lst[curr]
        lst[curr] -= lst[curr]
        # print(lst)
        curr += 1
    
    for val in lst:
        if val != 0:
            flag = True
            break

    if flag:
        print("NO")
    else:
        print("YES")

        