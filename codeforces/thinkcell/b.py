t = int(input())

for _ in range(t):
    n = int(input())
    # lst = [n-i for i in range(n-1)]
    pos = -1

    lst = []
    for i in range(n):
        if pos == -1:
            lst.append(n-(i//2))
        else:
            lst.append(i//2+1)
        pos *= -1

    print(" ".join(list(map(str, lst))))