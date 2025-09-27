


t = int(input())

def find_st(target, st, k):
    jump = len(target)
    if jump == 0:
        return k

    start = 0
    c = 0
    while True:
        start = st.find(target, start)
        if start == -1:
            break
        else:
            c += 1
        if c >= k:
            return c
        start += jump
    return c

for _ in range(t):
    n, low, high = list(map(int, input().split()))
    st = input()
    res = [0]*(high+2)


    for k in range(high, low-1, -1):
        r = n//k
        l = res[k+1]
        ans = 0
        while l <= r:
            mid = (r+l)//2
            c = find_st(st[:mid], st, k)
            if c >= k:
                ans = max(ans, mid)
                l = mid + 1
            else:
                r = mid - 1
        res[k] = ans
    
    print(" ".join(list(map(str, res[low:high+1]))))



    
