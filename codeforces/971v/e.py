
from collections import defaultdict, deque, Counter
import math



t = int(input())


for _ in range(t):
    n, k = list(map(int, input().split()))


    def compute(stop):
        left = stop*(stop+1)//2 + (stop+1)*k
        right = (stop+1+n-1)*(n-1-stop)//2 +(n-stop-1)*k

        return abs(left-right), left > right
    
    l, r = 0, n-1


    term = False
    ans = None

    while l <= r:
        mid = (l+r)//2
        res, dir = compute(mid)
        flag = True
        
        if res == 0:
            term = True
            ans = res
            break



        if mid > 0:
            res2, dir2 = compute(mid-1)
            if res2 < res and dir==dir2:
                r = mid-1
                # continue
            elif dir!=dir2:
                ans = min(res, res2)
                term = True
                break
            else:
                l = mid

        if mid < n-1:
            res2, dir2 = compute(mid+1)
            if res2 < res and dir==dir2:
                l = mid+1
                # continue
            elif dir!=dir2:
                ans = min(res, res2)
                term = True
                break
            else:
                r = mid

    
    if term:
        print(ans)
    else:
        ans, _ = compute(l)
        print(ans)