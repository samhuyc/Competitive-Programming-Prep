
t = int(input())

for _ in range(t):
    n, k = list(map(int, input().split()))
    vals = [None for _ in range(n)]
    l = 1
    r = n
    empty = 0
    curr = empty
    currleft = 1

    while True:

        if curr >= n:
            empty += 1
            curr = empty
            currleft *= -1
            if (empty >= n) or (vals[curr] != None):
                break
    
        if currleft == 1:
            vals[curr] = l
            l+= 1
            curr += k
        else:
            vals[curr] = r
            r -= 1
            curr += k
    
    print(" ".join(list(map(str, vals))))