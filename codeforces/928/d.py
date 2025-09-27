

t = int(input())

for _ in range(t):
    n = int(input())
    vals = list(map(int, input().split()))
    vals.sort()
    inverse = [2147483647-v for v in vals][::-1]
    ans = 0
    pointer = 0
    finished = 0
    matched = 0
    # print(vals, inverse)
    for i in range(n):
        curr = vals[i]

        while pointer < n and inverse[pointer] < curr:
            pointer += 1
        
        if pointer >= n:
            ans += 1
            continue
        
        if inverse[pointer] != curr:
            ans += 1
        else:
            matched += 1
            pointer += 1
    

    print(ans+matched//2)


