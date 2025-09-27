from sys import stdin

combo = input()
input()

d = {}
startnodes = []

for line in stdin:
    start, end = line.split("=")
    start = start[:-1]
    left = end.split(",")[0][2:]
    right = end.strip().split(",")[1][1:-1]
    d[start] = (left, right)
    if start[-1] == "A":
        startnodes.append(start)

n = len(combo)
totaltimes = []

for start in startnodes:
    count = 0
    visited = []
    while True:
        char = combo[count%n]
        if char == "L":
            start = d[start][0]
        else:
            start = d[start][1]
        count += 1
        if start[-1] == "Z":
            totaltimes.append(int(count/n))
            break
    
print(totaltimes)
ans = n
for val in totaltimes:
    ans *= val

print(ans)





    

    
    

