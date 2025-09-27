

t = int(input())

for _ in range(t):
    n, k = list(map(int, input().split()))
    if k == n:
        lst = ["1"]*n
        print(" ".join(lst))
    elif k == 1:
        lst = ["1"]*(n-1) + ["2"]
        print(" ".join(lst))
    else:
        print(-1)