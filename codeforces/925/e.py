import heapq


t = int(input())

for _ in range(t):
    n, m = list(map(int, input().split()))
    vals = list(map(int, input().split()))

    # nonz = []
    z = []
    totallength = 0

    for v in vals:
        count = 0
        st = str(v)
        length = len(st)
        totallength += length
        # good = 0

        for ind in range(-1, -n-1, -1):
            if st[ind] == "0":
                count += 1
            else:
                # if ind == -1:
                #     good = 1
                break

        if count != 0:
            heapq.heappush(z, -count)
    
    turn = -1
    while z:
        # print(totallength)
        curr = -heapq.heappop(z)
        if turn == -1:
            totallength -= curr
        turn *= -1
    
    if totallength > m:
        print('Sasha')
    else:
        print('Anna')




