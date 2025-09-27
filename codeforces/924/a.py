t = int(input())
for _ in range(t):
    a, b = list(map(int, input().split()))
    

    if a%2 != 0 and b %2 != 0:
        print("NO")
        continue

    if a%2 == 0 and b %2 == 0:
        print("YES")
        continue
    
    if a == b/2 or b == a/2:
        print("NO")
        continue
    else:
        print('YES')
    
    