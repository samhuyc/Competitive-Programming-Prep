
def main():
    t = int(input())

    for _ in range(t):
        test()

                
def test():
    n, m, k = list(map(int, input().split()))
    nl = list(map(int, input().split()))
    ml = list(map(int, input().split()))

    nl = sorted(nl)
    ml = sorted(ml)

    n, m = len(nl), len(ml)
    nunique = 0
    munique = 0
    good = 0
    nind = 0
    mind = 0
    curr = 1

    while True:
        if curr > k:
            good = 1
            break

        while nind < n and nl[nind] < curr:
            nind += 1
            
        while mind < m and ml[mind] < curr:
            mind += 1

        if (nind <n and nl[nind] == curr) and (mind < m and ml[mind] == curr):
            curr += 1
        elif nind <n and nl[nind] == curr:
            nunique += 1
            curr += 1
        elif mind <m and ml[mind] == curr:
            munique += 1
            curr += 1
        else:
            break
    
    if good== 1 and nunique <= k//2 and munique <= k//2:
        print('YES')
    else:
        print('NO')

main()
        
        

