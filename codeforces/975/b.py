


from collections import deque, Counter, defaultdict


t = int(input())

for _ in range(t):
    n, q = list(map(int, input().split()))
    vals = list(map(int, input().split()))
    query = list(map(int, input().split()))

    ans = defaultdict(int)
    
    used = -1

    for i in range(n):
        l, r = i+1, n-i
        freq = l*r -1
        ans[freq] += 1

        if i < n-1:
            lval = vals[i] + 1
            rval = vals[i+1] - 1
            if lval > rval:
                continue
            freq = (i+1)*(n-i-1)
            vcount = rval-lval + 1
            ans[freq] += vcount
            # print(lval, rval, freq)


    
    res = [0] * q
    for j in range(q):
        res[j] = ans[query[j]]
    
    print(" ".join(list(map(str, res))))
    
