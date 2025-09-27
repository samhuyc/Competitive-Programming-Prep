t = int(input())

for _ in range(t):
    n = int(input())
    vals = list(map(int, input().split()))
    info = []
    for i, v in enumerate(vals):
        double = 1 if len(str(v)) == 1 else 0
        for char in str(v):
            info.append((int(char), double, i))
    
    print(info)
    info.sort(key=lambda x:(x[0],x[1],x[2]))
    print(info)