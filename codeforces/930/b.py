t = int(input())

for _ in range(t):
    w = int(input())
    first = list(map(int, list(input())))
    second = list(map(int, list(input())))
    counter = 1
    uppos = None
    pos = None
    for curr in range(1, w):
        top = first[curr]
        bot = second[curr-1]
        if top == bot:
            counter += 1
        elif top < bot:
            counter = 1
            uppos = curr
        else:
            pos = curr
            break

    path = [first[0]]
    if pos != None:
        for i in range(1, pos):
            path.append(first[i])
        for j in range(pos-1, w):
            path.append(second[j])
    else:
        path = first
        path.append(second[-1])
    
    print("".join(list(map(str, path))))
    print(counter)

        
        
    

            



