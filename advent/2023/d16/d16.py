from sys import stdin
from collections import deque

mat = []

for line in stdin:
    line = line[:-1]
    mat.append(list(line))

height = len(mat)
width = len(mat[0])

record = []
startingPos = []

for i in range(width):
    startingPos.append((0, i, 1, 0))
    startingPos.append((height-1, i, -1, 0))  

for j in range(height):
    startingPos.append((j, 0, 0, 1))
    startingPos.append((j, width-1, 0, -1))


for s in startingPos:

    visited = [[[] for _ in range(width)] for _ in range(height)]
    tovisit = deque()
    tovisit.append(s)

    while tovisit:
        ypos, xpos, ydir, xdir = tovisit.popleft()
        if ypos < 0 or ypos >= height or xpos < 0 or xpos >= width:
            continue
        
        if [ydir, xdir] in visited[ypos][xpos]:
            continue
        else:
            visited[ypos][xpos].append([ydir, xdir])

        char = mat[ypos][xpos]

        if char == ".":
            tovisit.append((ypos+ydir, xpos+xdir, ydir, xdir))
            continue
        elif char == "\\":
            xdir, ydir = ydir, xdir
            tovisit.append((ypos+ydir, xpos+xdir, ydir, xdir))
            continue
        elif char == "/":
            xdir, ydir = -ydir, -xdir
            tovisit.append((ypos+ydir, xpos+xdir, ydir, xdir))
            continue
        elif char == "-":
            if ydir == 0:
                tovisit.append((ypos+ydir, xpos+xdir, ydir, xdir))
                continue
            else:
                tovisit.append((ypos, xpos-1, 0, -1))
                tovisit.append((ypos, xpos+1, 0, 1))
        elif char == "|":
            if xdir == 0:
                tovisit.append((ypos+ydir, xpos+xdir, ydir, xdir))
                continue
            else:
                tovisit.append((ypos-1, xpos, -1, 0))
                tovisit.append((ypos+1, xpos, 1, 0))       

    ans = 0
    for line in visited:
        for grid in line:
            if len(grid) > 0:
                ans += 1
    record.append(ans)

print(max(record))



    
