

import math
 
t = int(input())
 
 
for _ in range(t):
    n, m = list(map(int, input().split()))
    if m == 0:
        print(n)
        continue
 
    
 
    values = int(math.log2(m)+1)* "0" + bin(n)[2:]
    news = ""
    totalleng = len(values)
    for i in range(len(values)):
        currdigit = values[i]
        if currdigit == "1":
            news += currdigit
        else:
            if values[:i] == "" or int("0b" + values[:i], base =0) == 0:
                left = "0" + "1"* (totalleng-i)
            else:
                left = bin(int("0b" + values[:i], base =0)-1)[2:] + "1"* (totalleng-i)
            right = values[:i] + "1" + "0"*(totalleng - i -1)
            # print(i, values, left, right)
            dist = min(abs(int("0b" + right, base=0) - n), abs(int("0b"+left, base=0) -n))
            if dist <= m:
                news += "1"* (totalleng-i)
                break
            else:
                news += "0"
    
    print(int("0b" + news, base=0))
 