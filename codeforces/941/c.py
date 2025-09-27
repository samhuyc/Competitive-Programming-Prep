from collections import Counter


t = int(input())


for _ in range(t):
    n = int(input())
    piles = list(map(int, input().split()))
    piles = list(set(piles))
    piles.sort()
    count = 0

    # print(piles)
    if len(piles) == 1:
        print("Alice")
        continue

    accumulated = 0
    player = 0 ## 0 == Alice
    winner = None
    for v in piles:
        curr = v - accumulated
        if curr != 1 and winner == None:
            winner = player
        else:
            last = player
            player = 1 if player == 0 else 0
        accumulated += curr
    
    if winner == None:
        winner = last

    if winner == 0:
        print('Alice')
    else:
        print('Bob')



    

