

from collections import deque

t = int(input())


for _ in range(t):
    n, k, pb, ps = list(map(int, input().split()))

    perm = deque(list(map(int, input().split())))
    arr = deque(list(map(int, input().split())))
    perm.appendleft(0)
    arr.appendleft(0)
    amax = max(arr)
    pbvisited = [False] * (n+1)
    psvisited = [False] * (n+1)

    bbest = 0
    bcarry = 0
    for turn in range(1, k+1):
        bcarry += arr[pb]
        bcurrbest = arr[pb]*(k-turn) + bcarry
        bbest = max(bcurrbest, bbest)
        if arr[pb] == amax:
            break
        if pb == perm[pb] or pbvisited[perm[pb]] == True:
            break

        pbvisited[pb] = True
        pb = perm[pb]
    
    sbest = 0
    scarry = 0
    for turn in range(1, k+1):
        scarry += arr[ps]
        scurrbest = arr[ps]*(k-turn) + scarry
        sbest = max(scurrbest, sbest)
        if arr[ps] == amax:
            break

        if ps == perm[ps] or psvisited[perm[ps]] == True:
            break

        psvisited[ps] = True
        ps = perm[ps]
        
        
    
    if sbest == bbest:
        print('Draw')
    elif sbest > bbest:
        print("Sasha")
    else:
        print('Bodya')