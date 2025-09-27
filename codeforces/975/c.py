
import math



t = int(input())

for _ in range(t):
    n, k = list(map(int, input().split()))

    freqs = list(map(int, input().split()))

    tot = sum(freqs)
    atleastd = max(freqs)
    maxcards = min(tot + k, n*atleastd)

    ans = maxcards//atleastd
    if ans * atleastd >= tot:
        print(ans)
    else:
        x = maxcards
        y = tot
        b = atleastd
        kmin, kmax = 1, x//b
        vbest = math.inf
        for k in range(kmax, kmin-1, -1):
            vcurr = max(math.ceil(y/k),b)
            vmax = x//k
            if vcurr <= vmax:
                if vcurr < vbest:
                    vbest = vcurr
                if vbest == b:
                    break
        print(x//vbest)
    # print(tot, atleastd, maxcards, maxcards//atleastd)