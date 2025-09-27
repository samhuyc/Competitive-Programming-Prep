t = int(input())

for _ in range(t):
    n = int(input())
    px,py,qx,qy = list(map(int, input().split()))
    vals = list(map(int, input().split()))

    dist = ((px-qx)**2 + (py-qy)**2)**0.5

    if dist > sum(vals):
        print("No")
        continue

    if max(vals) > sum(vals) - max(vals) + dist:
        print("No")
    else:
        print('Yes')