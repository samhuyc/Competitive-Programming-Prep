from collections import defaultdict

t = int(input())

for _ in range(t):
    nlen = int(input())
    vals = list(map(int, input().split()))
    ma = max(vals)
    
    q = int(input())

    for _ in range(q):
        l, r = list(map(int, input().split()))
        curr = vals[l-1:r]
        seen = [0 for _ in range(ma+1)]
        
        first = None
        second = None

        for i, v in enumerate(curr):
            if seen[v] == 1:
                continue
            seen[v] = 1
            if first == None:
                first = (v, i+l-1)
            else:
                second = (v, i+l-1)
                break

        if second == None:
            print("-1 -1")
        else:
            print(f"{first[1]+1} {second[1]+1}")      
    print("")      
