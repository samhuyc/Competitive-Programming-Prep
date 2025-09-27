t = int(input())

for _ in range(t):
    n, m, k = list(map(int, input().split()))
    alst = list(map(int, input().split()))
    dlst = list(map(int, input().split()))
    flst = list(map(int, input().split()))
    diffs = []
    maxdiff = None
    singular = True

    for i in range(1, n):
        diffs.append((alst[i]-alst[i-1], alst[i-1], alst[i]))
        if maxdiff == None:
            maxdiff = alst[i]-alst[i-1]
        else:
            if maxdiff != alst[i]-alst[i-1]:
                singular = False

    
    diffs.sort(key=lambda x:(-x[0], x[1]))
    
    if singular:
        mod = diffs[0][0]
        base = diffs[0][1]
        for d in dlst:
            