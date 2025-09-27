t = int(input())

for _ in range(t):
    x, n = list(map(int, input().split()))

    target = x//n

    if x%n == 0:
        print(target)
        continue

    ans = 1
    for val in range(1,min(int(x**0.5), x//n)+1):
        if x%val == 0:
            ans = val
            if x%(x//val)==0 and x//val <= target:
                ans = x//val
                break
            
    print(ans)