

t = int(input())

for _ in range(t):

    
    n, m = list(map(int, input().split()))
    s = list(input())
    inds = list(map(int, input().split()))
    c = list(input())

    pos = list(set(inds))
    pos.sort()
    c.sort(reverse = False)
    c = c[:len(pos)]
    

    for i, ind in enumerate(pos):
        s[ind-1] = c[i]

    print(''.join(s))
