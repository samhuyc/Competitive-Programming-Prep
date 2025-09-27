


t = int(input())

def check(target, mainst):
    p = 0
    for char in mainst:
        if p < len(target) and target[p] == char:
            p += 1
    return p == len(target)


for _ in range(t):
    n, m = list(map(int, input().split()))
    a = list(input())
    b = list(input())


    l = 0
    r = min(n, m)

    while l <= r:
        
        mid = (l+r)//2
        
        target = a[:mid]
        response = check(target, b)
        # print(mid, response, target)
        if response:
            l = mid+1
        else:
            r = mid-1
    
    print(l-1)
    
