


t = int(input())

for _ in range(t):
    lst = list(input())
    a = 0
    b = 0
    for char in lst:
        if char == "A":
            a += 1
        else:
            b += 1
    if a > b:
        print("A")
    else:
        print("B")
