t = int(input())

for _ in range(t):
    n = int(input())
    vals = list(map(int, input().split()))

    target = vals[0]
    first = None
    last = None

    for i, v in enumerate(vals):
        if v != target:
            if first == None:
                first = i
            last = i
    
    if first == None:
        print(0)
        continue
    else:
        ans1 = last - first +1

    target = vals[-1]
    first = None
    last = None
    for i in range(-1, -n-1, -1):
        v = vals[i]
        if v != target:
            if first == None:
                first = i
            last = i
    ans2 = first - last + 1

    print(min(ans1, ans2))

        


