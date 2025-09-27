


import math

t = int(input())


for _ in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    c = 0
    b = []
    for i in range(n-1):
        curr = lst[i]
        nxt = lst[i+1]

        gcd = math.gcd(curr, nxt)
        b.append(gcd)


    breakind = None
    for i in range(len(b)-1):
        curr, nxt = b[i], b[i+1]
        if curr > nxt:
            breakind = i
            break

    if breakind == None:
        print("Yes")
        continue

    test1, test2, test3 = True, True, True
    lst1 = lst.copy()
    lst1.pop(breakind)
    lst2 = lst.copy()
    lst2.pop(breakind+1)
    lst3 = lst.copy()
    lst3.pop(breakind+2)
    # lst2 = lst[:breakind+1]+lst[breakind+2:]
    # lst3 = lst[:breakind+2]+lst[breakind+3:]
    
    # print(b)
    # print(lst1, lst2, lst3)

    b = []
    for i in range(n-2):
        curr = lst1[i]
        nxt = lst1[i+1]
        gcd = math.gcd(curr, nxt)
        b.append(gcd)

    for i in range(len(b)-1):
        curr, nxt = b[i], b[i+1]
        if curr > nxt:
            test1 = False
            break
    
    b = []


    for i in range(n-2):
        curr = lst2[i]
        nxt = lst2[i+1]
        gcd = math.gcd(curr, nxt)
        b.append(gcd)

    for i in range(len(b)-1):
        curr, nxt = b[i], b[i+1]
        if curr > nxt:
            test2 = False
            break
    b = []

    for i in range(n-2):
        curr = lst3[i]
        nxt = lst3[i+1]
        gcd = math.gcd(curr, nxt)
        b.append(gcd)

    for i in range(len(b)-1):
        curr, nxt = b[i], b[i+1]
        if curr > nxt:
            test3 = False
            break
    
    if test1 or test2 or test3:
        print("Yes")
    else:
        print("No")