
import math
t = int(input())

for _ in range(t):
    n = int(input())
    s = list(map(int, list(input())))
    count = [0]
    
    mat =[[0 for i in range(n)] for _ in range(n)]
    for i, char in enumerate(s):
        if char == 1:
            mat[0][i] = 1
    ans = 0
    for length in range(1, n):
        for end in range(length, n):
            gridmax = -math.inf
            for ind in range(end-length, end+1):
                indmin = math.inf
                for seglength in range(0, length):
                    for currind in range(ind, min(ind+seglength+1,end+1)):
                        indmin = min(mat[seglength][currind], indmin)
                gridmax = max(indmin, gridmax)
            mat[length][end] = gridmax
            ans += gridmax
    for line in mat:
        print(line)
    print(ans)



