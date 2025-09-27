t = int(input())


for _ in range(t):
    n = int(input())
    output = []

    mat = [[None for _ in range(n)] for _ in range(n)]

    singlesum = n*(n+1)//2
    x = int((n+1)/2)
    remain = 0
    for v in range(x+1, n+1):
        remain += v
    
    count= 0
    sum = 0
    # print(remain)

    for col in range(1, n+1):
        line = " ".join(list(map(str, range(1, n+1))))
        output.append(f"1 {col} {line}")
        sum += singlesum
        count += 1
    
    for row in range(1, x+1):
        line = " ".join(list(map(str, range(1, n+1))))
        output.append(f"2 {row} {line}")
        sum += singlesum - n*row
        count += 1
    
    for col in range(1, n+1):
        line = " ".join(list(map(str, range(1, n+1))))
        if (col*x)+remain < singlesum:
            output.append(f"1 {col} {line}")
            sum += singlesum - remain - x*col
            count += 1
    
    print(f"{sum} {count}")
    for line in output:
        print(line)