t = int(input())

for _ in range(t):
    n = int(input())
    st = list(input())
    removed = [False] * n
    a = ["p", 'i', 'e']
    b = ['m', 'a', 'p']
    ans = 0
    for i in range(n):
        if st[i-2:i+1] == a:
            removed[i-2] = True
            ans += 1
            # print(i)
    
    for j in range(n):
        if removed[j] == True:
            continue
        if st[j-2:j+1] == b:
            ans += 1
            # print(j)

    
    print(ans)
