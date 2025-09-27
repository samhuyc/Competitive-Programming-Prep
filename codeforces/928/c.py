import math

t = int(input())

for _ in range(t):
    n = int(input())
    sn = str(n)
    digits = int(math.log10(n))
    ans = 0
    for i in range(len(sn)-1):

        curr = int(sn[i])
        ans += curr*(int(sn[i+1:]))
        ans += curr*45*(10**(digits-i-1))
        print(curr, int(sn[i+1:]), (10**(digits-i-1)))
    
    for val in range(int(sn[-1])+1):
        ans += val

    print(ans)



