t = int(input())

for _ in range(t):
    n = int(input())
    if n % 2 == 1:
        print('NO')
        continue
    print('YES')
    lst = []
    curr = "AA"
    for i in range(0, n, 2):
        lst.append(curr)
        if curr == "AA":
            curr = "BB"
        else:
            curr = "AA"
    
    print("".join(lst))