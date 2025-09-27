t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    vals = [False] * (n+1)
    curr = 0
    p = []

    for v in a:
        if v > 0:
            p.append(curr)
            vals[curr] = True
            curr += 1
            while vals[curr] == True:
                curr += 1

        else:
            p.append(curr-v)
            vals[curr-v] = True
        
        # print(p, curr)
    print(" ".join(list(map(str, p))))

            