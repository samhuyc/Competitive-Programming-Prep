t = int(input())

for _ in range(t):
    n = int(input())
    s = list(map(int, list(input())))

    mat = []
    ans = 0
    for i in range(n):
        if i == 0:
            currcount = 0
            curr = []
            for char in s:
                if char == 1:
                    currcount += 1
                curr.append(currcount)
                ans += currcount //2 +1 if currcount %2 != 0 else currcount//2
            mat.append(curr)
        else:
            delta = mat[-1][i-1]

            curr = [0 for _ in range(n)]
            for j in range(i, n):
                curr[j] = mat[-1][j]-delta
                ans += curr[j] //2 +1 if curr[j] %2 != 0 else curr[j]//2
            mat.append(curr)
            

    for line in mat:
        print(line)
    print(ans)


