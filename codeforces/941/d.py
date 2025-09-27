import math


t = int(input())

for _ in range(t):
    n, k = list(map(int, input().split()))
    ans = [1]
    curr = 1

    while curr <= n/2:
        curr *= 2
        ans.append(curr)

    
    biggest = 2**(int(math.log(k, 2)))
    ans.remove(biggest)
    ans.append(k%biggest)
    if (biggest+1)*2 in ans:
        ans.remove(biggest*2)
    ans.append((biggest+1)*2-k%biggest)
    print(len(ans))
    print(' '.join(list(map(str, ans))))