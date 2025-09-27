import math


t = int(input())

for _ in range(t):
    k, x, a = list(map(int, input().split()))
    
    bets = 0
    record = [1]
    for i in range(x):
        if i==0:
            bets = 1
        else:
            # if bets % (k-1):
            curr = bets // (k-1) + 1
            
            # curr = math.ceil(bets/(k-1))
            record.append(curr)
            bets += curr
    
    remain = (a - bets)*k
    # print(k, x, a)
    if remain <= a:
        print('NO')
    else:
        print('YES')
    # print(record)


            
        
