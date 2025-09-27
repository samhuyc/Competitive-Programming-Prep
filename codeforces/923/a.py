t = int(input())

for _ in range(t):
    n = int(input())
    blocks = list(input().strip())
    start = None
    end = None
    for i, char in enumerate(blocks):
        if char == "B" and start == None:
            start = i
        if char == "B":
            end = i
    
    print(end - start + 1)

    