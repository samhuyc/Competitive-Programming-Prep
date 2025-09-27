from sys import stdin
from collections import Counter

records = [[] for _ in range(7)]
dic = {"T":10, "J":1, "Q":12, "K":13, "A":14}
for i in range(2, 10):
    dic[str(i)] = i

for line in stdin:
    hand, bid = line.split()
    vals = []
    for st in hand:
        vals.append(dic[st])
    c = Counter(vals)

    lst = c.most_common()
    newlst = []
    joker = 0
    for key, freq in lst:
        if key == 1:
            joker = freq
        else:
            newlst.append(freq)
    
    if joker == 5:
        combo = 5
        variation = 1
    else:
        combo = joker + newlst[0]
        variation = len(newlst)

    if variation == 5:
        loc = 6
    elif variation == 4:
        loc = 5
    elif variation == 3:
        if combo == 2:
            loc = 4
        else:
            loc = 3
    elif variation == 2:
        if combo == 3:
            loc = 2
        else:
            loc = 1
    else:
        loc = 0
    
    vals.append(int(bid))
    records[loc].append(vals)


records.reverse()
n = 1
ans = 0
for series in records:
    newseries = sorted(series)
    for hand in newseries:
        ans += hand[-1]*n
        n += 1

print(ans)

    











    
    
