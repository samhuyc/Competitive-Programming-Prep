import heapq
import math
import re
from itertools import combinations, permutations, product, combinations_with_replacement

from collections import deque, defaultdict,Counter




def check(cols, last):
    global winning
    leng = {ind: len(c) for ind, c in enumerate(cols)}

    for w in winning:
        good = True
        for colind, l in w:
            if leng[colind] < l:

    
    




def dfs(cols, it):
    if it%2 == 0:
        target = "F"
    else:
        target = "C"
    
    for ind, c in enumerate(cols):
        if c and c[-1] == target:
            cols[ind].pop()
            check(cols, ind)
            


        


    
    

def solve():
    ans = [False, False]
    _ = input()
    mat = [list(input()) for _ in range(6)]
    for line in mat:
        print(line)
    cols = [[] for _ in range(7)]

    global winning
    winning = []
    for y in range(6):
        for x in range(7):
            curr = []
            player = mat[y][x]
            if x + 3 < 7 and all(mat[y][x + d] == player for d in range(4)):
                ## hori
                winning.append([(x+d, 6-y) for d in range(4)])
            if y + 3 < 6 and all(mat[y+d][x] == player for d in range(4)):
                ## vert
                winning.append([(x, 6-y)])
            if y + 3 < 6 and x + 3 < 7 and all(mat[y+d][x+d] == player for d in range(4)):
                winning.append([(x+d, 6-y-d) for d in range(4)])
            if y + 3 < 6 and x - 3 >= 0 and all(mat[y+d][x-d] == player for d in range(4)):
                winning.append([(x-d, 6-y-d) for d in range(4)])

    for y in range(5, -1, -1):
        for x in range(7):
            cols[x].append(mat[y][x])

    dfs(cols, 0)

    return ans




def main():
    t = int(input())

    for case in range(t):
        ans = solve()
        print(f"Case #{case+1}: {ans}")

main()