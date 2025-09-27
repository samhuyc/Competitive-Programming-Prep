from collections import defaultdict
t = int(input())

def nested_defaultdict():
    return defaultdict(int)

for _ in range(t):
    n, x, y = list(map(int, input().split()))

    vals = list(map(int, input().split()))

    re = defaultdict(nested_defaultdict)

    for i, v in enumerate(vals):
        re[v%y][v%x]+=1
    
    ans1 = 0
    ans2 = 0
    for _, xre in re.items():
        for re, count in xre.items():
            if re == 0 or re==x/2:
                ans2 += count*(count-1)
            else:
                if x-re in xre:
                    ans1 += count *xre[x-re]

    print((ans1+ans2)//2)