t = int(input())

for _ in range(t):
    a, b, x, y = list(map(int, input().split()))
    if b == a:
        print(0)
        continue

    elif b < a:
        if (a ^ 1) != b:
            print(-1)
        else:
            print(y)
    
    else:
        if y > x:
            print((b-a)* x)
        else:
            diff = b-a
            if a % 2 == 1:
                # +1 first
                p = (diff +1)//2
                o = diff - p
                ans = p * x + o * y
            else:
                # ^ 1 first
                o = (diff+1)//2
                p = diff - o
                ans = p * x + o*y
            print(ans)
            