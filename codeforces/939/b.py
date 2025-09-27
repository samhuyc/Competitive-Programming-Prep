from collections import Counter


t = int(input())

for _ in range(t):
    n = int(input())
    cards = list(map(int, input().split()))

    c = list(dict(Counter(cards)).items())
    ans = 0

    for v, f in c:
        if f == 2:
            ans += 1
    
    print(ans)