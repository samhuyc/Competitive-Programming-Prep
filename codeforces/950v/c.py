


from collections import Counter, defaultdict

t = int(input())

for _ in range(t):
    n = int(input())
    alst = list(map(int, input().split()))
    blst = list(map(int, input().split()))
    m = int(input())
    vals = list(map(int, input().split()))

    endcounter = dict(Counter(blst))
    free = 0
    ans = True


    for i in range(-1, -n-1, -1):
        v = vals[i]
        if i == -1:
            nxt = -1
        else:
            nxt = vals[i-1]

        if v not in endcounter or endcounter[v] == 0:
            if free > 0:
                free -= 1
                endcounter[nxt] = 1
            else:
                ans = False
                break
        elif free > 0:
            free -= 1
            endcounter[v] += 1
        else:
            endcounter[v]-= 1
            free += 1
    
    

    if ans == False:
        print('No')
        continue
    
    flag = 0
    for i, v in enumerate(alst):
        if v != blst[i]:
            flag += 1
    
    print(free, flag)

    if flag > free:
        print("No")
    else:
        print("Yes")


