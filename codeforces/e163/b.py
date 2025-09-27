t = int(input())

for _ in range(t):
    n = int(input())
    vals = list(map(int, input().split()))
    flag = False

    while True:
        good = True
        for i in range(1, len(vals)):
            curr, prev = vals[i], vals[i-1]
            if prev > curr:
                good = False
                if len(str(prev)) == 1 and len(str(curr)) == 1:
                    # print('enter')
                    flag = True
                    break
                else:
                    newvals = vals[:i-1] + list(map(int, list(str(prev)))) + vals[i:]
                    vals = newvals
                    # print(vals, good, flag)
                    break
        
        if flag or good:
            break
    
    if flag == False:
        print('yes')
    else:
        print('No')
    
                    









            

                
