t = int(input())

for _ in range(t):
    n = int(input())
    trace = list(map(int, input().split()))
    curr = [0 for _ in range(26)]

    record = []
    for count in trace:
        for i, val in enumerate(curr):
            if val == count:
                curr[i] += 1
                record.append(chr(i+97))
                break
    
    print("".join(record))
    
        