t = int(input())

for _ in range(t):
    n = int(input())

    prev = set()

    for _ in range(n):
        row = list(input())
        c = 0
        for char in row:
            if char == "1":
                c += 1
        if c != 0:
            prev.add(c)
    
    if len(list(prev)) != 1:
        print("TRIANGLE")
    else:
        print('SQUARE')