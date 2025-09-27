t = int(input())

for _ in range(t):
    n, k = list(map(int, input().split()))
    mat = []
    for _ in range(n):
        info = list(map(int, input().split()))
        add = [None] * (n-len(info))
        info = add + info
        mat.append(info)
    
    vals = [0] * n

    vals[-1] = max(0, mat[-1][-1])
    
    for row in range(-2, -n-1):
        rowmax = 0
        for col in range(-1, row-1):
            if col == -1:
                rowmax = max(rowmax, mat[row][col])
            else:
                curr = max(vals[col+1]+mat[row][col], vals[col+1])
                rowmax = max(rowmax, curr)
        vals[row] = rowmax
    
    print(vals)

