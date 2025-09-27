t = int(input())

for _ in range(t):
    n = int(input())
    mat = []
    mat.append(list(input()))
    mat.append(list(input()))

    curr = n-1
    row = 1
    flag = False
    while True:
        print(curr, row)
        if row == 0 and curr == 0:
            flag = True
            break
        if mat[row][curr-1] == ">":
            curr -= 1
            continue
        newrow = 1 if row == 0 else 0
        if mat[newrow][curr-1] == ">":
            row = newrow
            curr -= 1
            continue
        break
    
    if flag:
        print('yes')
    else:
        if row == 1 and curr == 0:
            print("yes")
        else:
            print('no')
        
