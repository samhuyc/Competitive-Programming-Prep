

t = int(input())


for _ in range(t):
    n = int(input())

    vals = list(map(int, input().split()))

    su = sum(vals)
    ans = 0
    c = 0
    for i in range(n):
        curr = vals[i]
        su -= curr
        ans += curr * su
        c += n-i-1
    
    M = 10**9 + 7

    def mod_inverse(Q, M):
        def extended_gcd(a, b):
            if a == 0:
                return b, 0, 1
            
            gcd, x1, y1 = extended_gcd(b % a, a)
            x = y1 - (b // a) * x1
            y = x1
            return gcd, x, y

        gcd, x, y = extended_gcd(Q, M)
        return x % M

    print(((ans%M)*mod_inverse(c, M))%M)



