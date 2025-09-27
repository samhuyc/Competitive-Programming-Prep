t = int(input())

for _ in range(t):
    n = int(input())
    vals = list(map(int, input().split()))
    total = sum(vals)

    if total % n != 0:
        print("NO")
        continue

    target = total/n
    carry = 0
    finished = 1

    for i in range(n):
        curr = vals[i]
        curr += carry

        if curr < target:
            finished = 0
            break
        else:
            carry = curr - target
    
    if finished == 0:
        print("NO")
    else:
        print("YES")