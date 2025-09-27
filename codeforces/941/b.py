

t = int(input())

for _ in range(t):
    n, m = list(map(int, input().split()))
    mat = []
    for _ in range(n):
        line = list(input())
        mat.append(line)


    target = ['W', 'B']
    ans = False
    for color in target:

        firstr = False
        firstc = False
        lastr = False
        lastc = False

        if color in mat[0]:
            firstr = True
        if color in mat[-1]:
            lastr = True
        for i in range(n):
            curr = mat[i][0]
            if curr == color:
                firstc = True
                break
        for j in range(n):
            curr = mat[j][-1]
            if curr == color:
                lastc = True
                break
        
        if firstr and lastr and firstc and lastc:
            ans = True
            
    if ans:
        print('YES')
    else:
        print('NO')