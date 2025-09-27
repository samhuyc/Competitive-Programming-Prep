t = int(input())

for _ in range(t):
    n, k = list(map(int, input().split()))
    if k <= 4*n-4:
        ans = k//2+1 if k%2 != 0 else k//2
        print(ans)
    else:
        ans = (k-4*n+4)+(2*n-2)
        print(ans)


