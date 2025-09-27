from sys import stdin

ans = 0
for line in stdin:
    vals = list(map(int, line.split()))
    record = [vals[0]]
    while True:
        newvals = [vals[i]- vals[i-1] for i in range(1, len(vals))]
        found = True
        for v in newvals:
            if v != 0:
                found = False
                break
        if found:
            break
        record.append(newvals[0])
        vals = newvals
    
    curr = 0
    for i in range(-1, -len(record)-1, -1):
        curr = record[i] - curr
    ans += curr
print(ans)

    
