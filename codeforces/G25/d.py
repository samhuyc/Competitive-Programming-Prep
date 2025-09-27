t = int(input())

for _ in range(t):
    n, k = list(map(int, input().split()))
    stalls = []
    if n % k == 0:
        print("YES")
        print(1)
        print(str(n//k))
        continue
    

    
    v = list(map(int, list(bin(n)[2:])))
    look = [None] * (len(v))
    sum = 0
    for i in range(-1, -len(v)-1, -1):
        sum += v[i]
        look[i] = sum
    
    look.append(0)
    look.pop(0)

    good = False
    sum = 0
    for i, char in enumerate(v):
        currlook = look[i]
        if char+ 2*sum + currlook == k:
            good = True
            pos = i
            break

        sum = 2*sum + char


    if good:
        maxpow = len(v)-1
        for i in range(pos, len(v)):
            if v[i] == 1:
                stalls.append(2**(maxpow-i))
        print("YES")
        print(len(stalls))
        print(' '.join(list(map(str, stalls))))
    else:
        print("NO")
            





    
