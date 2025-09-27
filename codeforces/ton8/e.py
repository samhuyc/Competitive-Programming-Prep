from math import comb

t = int(input())

for _ in range(t):
    l, n = list(map(int, input().split()))
    ans = 0
    for i in range(1, l-2*n):
        items = i
        out = l-2*n-i
        bags = n
        ans += ((comb(items+bags-1, bags-1)//2)%998244353)*(comb(out+n, n)%998244353)
    print(ans)



