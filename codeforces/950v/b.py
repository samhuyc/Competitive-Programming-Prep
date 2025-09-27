
from collections import Counter, defaultdict

t = int(input())

for _ in range(t):
    n, f, k = list(map(int, input().split()))
    vals = list(map(int, input().split()))
    # print(vals)
    target = vals[f-1]
    vals.sort(reverse = True)


    if k == n:
        print("YES")
        continue

    if vals[k-1] > target:
        print("No")
    elif vals[k-1] == target and vals[k] == target:
        print("Maybe")
    else:
        print("Yes")

