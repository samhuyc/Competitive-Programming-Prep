from collections import deque

t = int(input())

for _ in range(t):
    n, m = list(map(int, input().split()))
    vals = list(map(int, input().split()))
    commands = list(input())

    newv = deque()
    l = 0
    r = n-1
    for c in commands:
        if c == "L":
            newv.appendleft(vals[l])
            l += 1
        else:
            newv.appendleft(vals[r])
            r -= 1
    
    v = list(newv)
    ans = deque()
    curr = 1
    for val in v:
        curr *= val
        curr = curr%m
        ans.appendleft(curr)
    
    ans = list(map(str, list(ans)))
    print(' '.join(ans))


