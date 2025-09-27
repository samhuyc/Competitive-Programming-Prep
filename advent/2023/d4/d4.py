from sys import stdin

cards = [1 for _ in range(1000)]

for i, line in enumerate(stdin):
    l1, l2 = line.split("|")
    target = l1.split(":")[1].split()
    vals = l2.split()
    count = 0
    for t in target:
        for v in vals:
            if t == v:
                count+= 1

    for j in range(1, count+1):
        cards[i+j] += cards[i]




print(sum(cards[:i+1]))

