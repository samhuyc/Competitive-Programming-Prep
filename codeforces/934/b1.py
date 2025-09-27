from collections import Counter
t = int(input())

for _ in range(t):
    n, k = list(map(int, input().split()))
    lst = list(map(int, input().split()))
    left = lst[:n]
    right = lst[n:]
    
    cleft = list(dict(Counter(left)).items())
    cright = list(dict(Counter(right)).items())

    l = []
    r = []
    need = 2*k
    count = 0
    used = {}
    for v, f in cleft:
        if need == 0:
            break
        if f == 2:
            l.append(v)
            l.append(v)
            used[v] = True
            need -= 2
            count += 1
    
    for v, f in cright:
        if count == 0:
            break
        if f == 2:
            r.append(v)
            r.append(v)
            used[v] = True
            count -= 1

    for i in range(1, n+1):
        if need == 0:
            break
        if i not in used:
            l.append(i)
            r.append(i)
            need -= 1

    
    print(" ".join(list(map(str, l))))
    print(" ".join(list(map(str, r))))


        