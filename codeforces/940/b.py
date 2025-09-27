

t = int(input())
for _ in range(t):
    n, k = list(map(int, input().split()))
    

    if n == 1:
        print(k)
        continue
    

    start = 0
    while k > 2**start - 1:
        start += 1
    
    ans = []
    ans.append(2**(start-1)-1)
    remain = k - 2**(start-1) + 1
    ans.append(remain)
    if n == 2:
        print(f'{ans[0]} {ans[1]}')
        continue
    
    for i in range(2, n):
        ans.append(0)
    
    print(" ".join(list(map(str, ans))))