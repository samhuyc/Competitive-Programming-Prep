


t = int(input())

for _ in range(t):

    n, x = list(map(int, input().split()))

    alst = list(map(int, input().split()))

    curr = set([x])

    ans = 1

    for v in alst:
        if v == 1 or v > x or x % v != 0:
            # print(v, curr)
            continue

        if v in curr:
            ans += 1
            curr = set([x, x//v])
        else:
            rec = list(curr)
            for element in rec:
                if element % v == 0:
                    curr.add(element//v)
        # print(v, curr)
    
    print(ans)
