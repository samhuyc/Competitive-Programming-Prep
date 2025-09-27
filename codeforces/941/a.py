from collections import Counter, deque


t = int(input())


for _ in range(t):
    n, k = list(map(int, input().split()))
    cards = list(map(int, input().split()))
    c = list(dict(Counter(cards)).items())
    results = []
    for v, f in c:
        results.append(f)

    results.sort(reverse=True)
    results = deque(results)
    removed = 0

    while results and results[0] >= k:
        curr  = results.popleft()
        curr_removed = curr // k
        curr -= curr_removed
        if curr >= k:
            results.appendleft(curr)
        else:
            if results:
                results[0] += curr
            else:
                results.appendleft(curr)
                break
    
    ans = 0
    for v in results:
        ans += v
    
    print(ans)
    
