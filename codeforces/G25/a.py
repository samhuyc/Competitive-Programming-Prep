t = int(input())

for _ in range(t):
    n = int(input())
    info = input().split("0")
    c = 0
    newinfo = []
    for char in info:
        if len(char) > 0:
            newinfo.append(len(char))
    
    if newinfo == [2]:
        print('No')
        continue


    for char in info:
        if len(char) == 0:
            continue

        if len(char) == 2:
            c += 2
        elif len(char) % 2 == 1:
            c += 1
        else:
            c += 0

    if c % 2 == 0:
        print('YES')
    else:
        print("NO")

