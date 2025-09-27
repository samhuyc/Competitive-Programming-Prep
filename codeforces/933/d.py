t = int(input())

for _ in range(t):
    n, m, x = list(map(int, input().split()))
    player = [False] * n
    player[x-1] = True

    for _ in range(m):
        info = list(input().split())
        dist = int(info[0])
        new = [False] * n

        if info[1] == "0":
            for i, p in enumerate(player):
                if p == True:
                    loc = (i+dist)%n
                    new[loc] = True
        
        elif info[1]== '1':
            for i, p in enumerate(player):
                if p == True:
                    loc = (i-dist)%n
                    new[loc] = True

        else:
            for i, p in enumerate(player):
                if p == True:
                    loc1 = (i-dist)%n
                    loc2 = (i+dist)%n
                    new[loc1] = True 
                    new[loc2] = True
        
        player = new
    
    final = []
    count = 0
    for i, v in enumerate(player):
        if v == True:
            final.append(i+1)
            count += 1
    
    print(count)
    print(" ".join(map(str, final)))



