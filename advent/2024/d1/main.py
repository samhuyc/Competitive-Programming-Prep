
from collections import defaultdict
from sys import stdin

l1, l2 = [], []
di = defaultdict(int)

for line in stdin:
    a, b = list(map(int, line.split()))
    l1.append(a)
    l2.append(b)
    di[b] += 1

    
ans = 0
for a in l1:
    ans += a * di[a]
print(ans)