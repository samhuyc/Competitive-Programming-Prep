

from collections import Counter, defaultdict

t = int(input())

for _ in range(t):
    n, m = list(map(int, input().split()))
    c = dict(Counter(list(input())))
    ans = 0
    for diff in ["A", "B", "C", "D", "E", "F", "G"]:
        if diff in c:
            if c[diff] < m:
                ans += m - c[diff]
        else:
            ans += m
    print(ans)

    
