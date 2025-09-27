t = int(input())

for _ in range(t):
    n = int(input())
    lst = list(map(int, input().split()))

    s = set()
    vals = [v+i+1 for i, v in enumerate(lst)]
    # print(vals)
    count = 0
    prev = None
    for i in range(-1, -n-1, -1):

        curr = vals[i]
        if prev == None:
            prev = curr
        if prev == curr:
            count += 1
        else:
            for delta in range(count):
                s.add(prev-delta)
                count = 1
        prev = curr
        # print(curr, count)
    
    if count != 0:
        # print(count)
        for delta in range(count):
            # print(curr-delta)
            s.add(curr-delta)
    
    vals = list(s)
    vals.sort(reverse=True)
    # print(vals)
    ans = list(map(str, vals))

    print(" ".join(ans))
