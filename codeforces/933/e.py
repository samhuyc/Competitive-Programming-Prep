import heapq

t = int(input())

for _ in range(t):
    n, m, k, d = list(map(int, input().split()))
    record = []

    for _ in range(n):
        hp = []
        heapq.heappush(hp,(1, 0))
        vals = list(map(int, input().split()))
        ans = sum(vals)

        for i in range(1,m):
            currsupp = vals[i]

            while hp[0][1] < i-d-1:
                heapq.heappop(hp)
            
            currcost = currsupp + hp[0][0] + 1
            heapq.heappush(hp,(currcost,i))
            # print(i, hp)
        
        record.append(currcost)

    total = sum(record[:k])
    ans = total
    for i in range(k, n):
        total -= record[i-k]
        total += record[i]
        ans = min(total, ans)
    print(ans)


