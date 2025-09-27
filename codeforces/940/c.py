import math

t = int(input())

fact = [None] * (3*10**5)
prev = 1
for i in range(1, len(fact), 2):
    prev *= i%(10**9+7)
    fact[i] = prev



def xchoosey(x, y):
    diff = min(x-y,y)
    top = 1
    bot = 1
    for i in range(diff):
        top *= x-i%(10**9+7)
    for j in range(diff):
        bot *= 1+j%(10**9+7)

    return (top//bot)%(10**9+7)



for _ in range(t):
    n, k = list(map(int, input().split()))
    moves = []
    new_n = n
    for _ in range(k):
        a, b = list(map(int, input().split()))
        if a == b:
            new_n -= 1
        else:
            new_n -= 2
    
    ans = 0
    if new_n %2 == 0:
        for diagonal in range(0, new_n+1, 2):
            curr = 1
            curr *= xchoosey(new_n, diagonal)%(10**9+7)
            curr *= (2**((new_n-diagonal)//2)%(10**9+7))
            curr *= fact[new_n-diagonal-1]
            ans += curr%(10**9+7)

    else:
        for diagonal in range(1, new_n+1, 2):
            curr = 1
            curr *= xchoosey(new_n, diagonal)%(10**9+7)
            curr *= (2**((new_n-diagonal)//2)%(10**9+7))
            curr *= fact[new_n-diagonal-1]
            ans += curr%(10**9+7)

    print(ans%(10**9+7))