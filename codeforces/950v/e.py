


t = int(input())



for _ in range(t):

    n, m = list(map(int, input().split()))

    amat = [list(map(int, input().split())) for _ in range(n)]
    bmat = [list(map(int, input().split())) for _ in range(n)]

    rowa = [None] * (n*m+1)
    rowb = [None] * (n*m+1)
    cola = [None] * (n*m+1)
    colb = [None] * (n*m+1)

    for col in range(m):
        for row in range(n):
            rowa[amat[row][col]] = row


    for row in range(n):
        target = rowa[bmat[row][0]]
        for col in range(m):
            rowb[bmat[row][col]] = target

    for col in range(m):
        for row in range(n):
            cola[amat[row][col]] = col
    
    for col in range(m):
        target = cola[bmat[0][col]]
        # print(bmat[0][col], target)
        for row in range(n):
            colb[bmat[row][col]] = target

    if rowa == rowb and cola == colb:
        print("Yes")
    else:
        print("No")
    
    # print(rowa, rowb)
    # print(cola, colb)