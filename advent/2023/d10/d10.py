from sys import stdin
from collections import deque

mat = []
loc = None
for line in stdin:
    mat.append(list(line)[:-1])
    if "S" in list(line):
        loc = [len(mat)-1, list(line).index("S")]

#mat[loc[0]][loc[1]] = "F"
mat[loc[0]][loc[1]] = "J"
height = len(mat)
width = len(mat[0])

valsmat = [[None for _ in range(width)] for _ in range(height)]

for y in range(loc[0]-1, loc[0]+2):
    print(mat[y][loc[1]-1:loc[1]+2])


#valsmat[loc[0]][loc[1]] = "F"
valsmat[loc[0]][loc[1]] = "J"
prevloc = loc
#nxtloc = [loc[0], loc[1]+1]
nxtloc = [loc[0], loc[1]-1]

while nxtloc != loc:
    temp = nxtloc.copy()
    curr = mat[temp[0]][temp[1]]
    valsmat[temp[0]][temp[1]] = curr

    if curr == "|":
        if [nxtloc[0]-1, nxtloc[1]] == prevloc:
            nxtloc[0] += 1
        else:
            nxtloc[0] -= 1
            
    elif curr == "-":
        if [nxtloc[0], nxtloc[1]-1] == prevloc:
            nxtloc[1] += 1
        else:
            nxtloc[1] -= 1
            
    elif curr == "L":
        if [nxtloc[0]-1, nxtloc[1]] == prevloc:
            nxtloc[1] += 1
        else:
            nxtloc[0] -= 1

    elif curr == "J":
        if [nxtloc[0]-1, nxtloc[1]] == prevloc:
            nxtloc[1] -= 1
        else:
            nxtloc[0] -= 1
        
    elif curr == "7":
        if [nxtloc[0]+1, nxtloc[1]] == prevloc:
            nxtloc[1] -= 1
        else:
            nxtloc[0] += 1

    elif curr == "F":
        if [nxtloc[0]+1, nxtloc[1]] == prevloc:
            nxtloc[1] += 1
        else:
            nxtloc[0] += 1
    
    prevloc = temp

ans = 0
for y in range(height):
    for x in range(width):
        if valsmat[y][x] is None:
            count = 0
            for neighborx in range(0, x):
                if valsmat[y][neighborx] in ["|", "L", "J"]:
                    count += 1
            if count % 2 != 0:
                ans += 1

print(ans)



