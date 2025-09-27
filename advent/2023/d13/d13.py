from sys import stdin

graphs = []
curr = []
for line in stdin:
    if line != "\n":
        curr.append(line[:-1])
    else:
        graphs.append(curr)
        curr = []

graphs.append(curr)

ans = 0
for g in graphs:
    height = len(g)
    width = len(g[0])

    for cRow in range(1, height):
        error = 0
        for change in range(1, height):
            if cRow - change >= 0 and cRow + change - 1 < height:
                for i in range(width):
                    if g[cRow - change][i] != g[cRow + change - 1][i]:
                        error += 1
        if error == 1:
            ans += 100*cRow
            break
    
    for cColumn in range(1, width):
        error = 0
        for change in range(1, width):
            if cColumn - change >= 0 and cColumn + change - 1 < width:
                for i in range(height):
                    if g[i][cColumn - change] != g[i][cColumn + change - 1]:
                        error += 1
        if error == 1:
            ans += cColumn
            break

print(ans)






        

        
