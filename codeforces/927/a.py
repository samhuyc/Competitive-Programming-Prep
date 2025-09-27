

t = int(input())

for _ in range(t):
    n = int(input())
    info = list(input())

    curr = 0
    ans = 0
    while curr < n:
        if info[curr]== "@":
            ans += 1

        if curr < n-2 and info[curr+2]== "*" and info[curr+1] == "*":
            break
        elif curr < n-1 and info[curr+1] == "*":
            curr += 2
        elif curr < n-2 and info[curr+2] == "*":
            curr += 1
        else:
            curr += 1
    
    print(ans)



        
