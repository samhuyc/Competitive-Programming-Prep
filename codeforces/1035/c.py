t = int(input())

for _ in range(t):
    n,l,r,k = list(map(int, input().split()))

    if n % 2 == 1:
        print(l)
        continue
    if n == 2:
        print(-1)
        continue


    ex = len(bin(l)[2:]) 
    nxt = 2**ex
    curr = l
    # print(curr, nxt)
    if nxt > r:
        print(-1)
        continue
    if k <= n - 2:
        print(curr)
    else:
        print(nxt)
