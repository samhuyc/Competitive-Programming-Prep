t = int(input())

for _ in range(t):
    a, b, r = list(map(int, input().split()))
    abin = list(map(int, list(bin(a)[2:])))
    bbin = list(map(int, list(bin(b)[2:])))
    rbin = list(map(int, list(bin(r)[2:])))
    vals = [[0 for _ in range(max(len(abin), len(bbin), len(rbin)))] for _ in range(3)]

    for i in range(-1, -max(len(abin), len(bbin), len(rbin))-1, -1):
        if -i <= len(abin):
            vals[0][i]= abin[i]
        if -i <= len(bbin):
            vals[1][i] = bbin[i]
        if -i <= len(rbin):
            vals[2][i] = rbin[i]   

    seen = 0
    ans1= 0
    ans2 = 0
    l = len(vals[0])
    for i in range(l):
        if vals[2][i] == 1:
            seen = 1
        
        if seen:
            if vals[0][i] != vals[1][i]:
                diff = 2**(l-i-1)
                ans1 = abs(diff-abs(ans1))

        else:
            if vals[0][i] > vals[1][i]:
                ans1 += 2**(l-i-1)
            elif vals[0][i] < vals[1][i]:
                ans1 -= 2**(l-i-1)     
    
    print(ans1)

        





