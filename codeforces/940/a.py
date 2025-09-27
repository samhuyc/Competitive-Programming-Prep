from collections import Counter

t = int(input())


for _ in range(t):
    n = int(input())
    vals = list(map(int, input().split()))
    c = list(dict(Counter(vals)).items())
    ans = 0
    for v, f in c:
        ans += f//3
    
    print(ans)