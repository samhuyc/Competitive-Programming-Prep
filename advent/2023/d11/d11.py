from sys import stdin

mat = []
galaxies = []
row = 0

for line in stdin:

    mat.append(list(line)[:-1])
    for i, char in enumerate(list(line)[:-1]):
        if char == "#":
            galaxies.append([row, i])
    row += 1

rowE = []
colE = []

for row, line in enumerate(mat):
    if "#" not in line:
        rowE.append(row)

for x in range(len(mat[0])):
    expand = True
    for y in range((len(mat))):
        if mat[y][x] == "#":
            expand = False
            break
    if expand:
        colE.append(x)

print(rowE, colE)

for i, [y, x] in enumerate(galaxies):
    newx, newy = x, y
    for c in colE:
        if c < x:
            newx += 999999
    for r in rowE:
        if r < y:
            newy += 999999
    
    galaxies[i] = [newy, newx]


ans = 0
n = len(galaxies)
for i in range(n):
    first = galaxies[i]
    for j in range(i+1, n):
        second = galaxies[j]
        ans += abs(first[0]-second[0])+abs(first[1]-second[1])

print(ans)

