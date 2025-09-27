import heapq


t = int(input())

for _ in range(t):
    n, m = list(map(int, input().split()))
    vals = list(map(int, input().split()))

    z = []
    totallength = 0

    for v in vals:
        count = 0
        st = str(v)
        length = len(st)
        totallength += length

        for ind in range(-1, -n-1, -1):
            if st[ind] == "0":
                count += 1
            else:
                break

        if count != 0:
            z.append(count)
    
    z.sort(reverse=True)
    turn = -1
    for val in z:
        if turn == -1:
            totallength -= val
        turn *= -1
    
    if totallength > m:
        print('Sasha')
    else:
        print('Anna')
    