
def solve():
    R, C, k = list(map(int, input().split()))
    N = R*C
    counts = [0] * (N+1)
    mat = []
    for _ in range(R):
        line = list(map(int, input().split()))
        mat.append(line)
        for b in line:
            counts[b] += 1

    totpairs = N*(N-1)
    diffpairs = totpairs - sum([v*(v-1) for v in counts if v > 0])
    dist = [0] * (max(R, C)+1)

    for di in range(R):
        for dj in range(C):
            if di == 0 and dj == 0:
                continue
            cnt = (R - di) * (C - dj)
            if di != 0 and dj != 0:
                cnt *= 2
            d = max(di, dj)
            dist[d] += cnt

    r = diffpairs / totpairs
    diff_owner_pairs_at_d = [cnt * r * 2 for cnt in dist]

    cumulative = 0
    for d in range(1, max(R, C)+1):
        cumulative += diff_owner_pairs_at_d[d]
        if cumulative + 1e-10 >= k:
            return d
    
    return max(R, C) - 1


def main():
    t = int(input())
    for case in range(t):
        result = solve()
        print(f"Case #{case+1}: {result}")

main()
