
from collections import Counter
import math

t = int(input())


for _ in range(t):
    n = int(input())

    st = list(input())

    if len(st)%2 == 0:
        odd, even = [st[i] for i in range(0, n, 2)], [st[i] for i in range(1, n, 2)]
        lst1 = len(odd) -Counter(odd).most_common(1)[0][1]
        lst2 = len(even) -Counter(even).most_common(1)[0][1]
        print(lst1 + lst2)
        continue

    frontup, frontdown, backup, backdown = [0]*26, [0]*26, [0]*26, [0]*26
    odd, even = [st[i] for i in range(0, n, 2)], [st[i] for i in range(1, n, 2)]
    for char in even:
        frontup[ord(char)-97] += 1
    for char in odd:
        frontdown[ord(char)-97] += 1

    ans = math.inf
    total = len(st)-1
    def find(frontup, frontdown, backup, backdown):
        tempup, tempdown = [0]*26, [0]*26
        upmax, downmax = 0, 0
        for i in range(26):
            tempup[i] = frontup[i] + backdown[i]
            upmax = max(upmax, tempup[i])
            tempdown[i] = frontdown[i] + backup[i]
            downmax = max(downmax, tempdown[i])
        return total - upmax - downmax
    
    for i in range(total, -1, -1):
        currchar = st[i]
        # print(frontup, frontdown, backup, backdown)
        if i%2 == 1:
            frontup[ord(currchar)-97] -= 1
            re = find(frontup, frontdown, backup, backdown)
            ans = min(ans, re)
            backup[ord(currchar)-97] += 1
        else:
            frontdown[ord(currchar)-97] -= 1
            re = find(frontup, frontdown, backup, backdown)
            ans = min(ans, re)
            backdown[ord(currchar)-97] += 1
        # print(frontup, frontdown, backup, backdown)
    
    print(ans+1)
    



    

