t = int(input())

for _ in range(t):
    n, m, k = list(map(int, input().split()))

    left = list(map(int, input().split()))
    right = list(map(int, input().split()))
    ans = 0
    for l in left:
        count = 0
        target = k - l
        for r in right:
            if r <= target:
                ans += 1
    
    print(ans)