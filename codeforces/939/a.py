t = int(input())

for _ in range(t):
    k, q = list(map(int, input().split()))
    aval = list(map(int, input().split()))
    nval = list(map(int, input().split()))
    ans = []
    a = aval[0]
    for n in nval:
        if n == a:
            ans.append(n-1)
        elif n > a:
            ans.append(a-1)
        else:
            ans.append(n)
    print(" ".join(list(map(str, ans))))



