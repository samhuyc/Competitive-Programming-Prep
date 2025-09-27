from sys import stdin
from collections import deque

y, x = 0, 0
hedges = {}
vedges = {}
mini = 100000000000
maxi = -10000000000

for line in stdin:
    line = line[:-1]
    _, _, info = line.split()
    info = info[1:-1]
    n = int(info[1:-1], 16)
    dir = int(info[-1])

    if dir == 0 or dir == 2:
        if dir == 0:
            hedges[y] = (x, x+n)
            x = x+n
        else:
            hedges[y] = (x-n, x)
            x = x-n
        mini = min(x, mini)
        maxi = max(x, maxi)

        
    else:
        if dir == 1:
            vedges[x] = (y, y+n)
            y = y+n
        else:
            vedges[x] = (y-n, y)
            y = y-n


ans = 0
edges = list(hedges.items())
edges.sort()

ans = 0
for i in range(mini, maxi+1):
    currheight = None
    met = 0
    for edge in edges:
        height, (start, end) = edge
        if start <= i and end >= i:
            if met == 0:
                currheight = height
                met += 1
                continue
            if met % 2 > 0:
                ans += (height - currheight)+1
                met += 1
            else:
                ans -= (height - currheight)-1
                met += 1

print(edges)
print(ans)


        








    




