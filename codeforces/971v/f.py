
from collections import defaultdict, deque, Counter
import math



t = int(input())


for _ in range(t):
    n, q = list(map(int, input().split()))
    vals = list(map(int, input().split()))

    lookup = [0] * (n+1)
    total = sum(vals)
    su = 0
    for i in range(n):
        su += vals[i]
        lookup[i+1] = su
    
    def compute(l, r):
        if l % n == 0:
            lbefore = (l-1)//n
            lind = n
        else:
            lbefore = l//n
            lind = l%n
        
        lshift = lbefore + 1
        lxa = (lind + lshift - 1)%n
        if lxa == 0:
            lxa = n
        endpos = n - lshift + 1

        if endpos >= lind:
            lsum = total - lookup[lxa-1] + lookup[lshift-1]
        else:
            lsum = lookup[lshift-1] - lookup[lxa-1]

        # print(lbefore, lind, lxa, lshift, endpos, lsum)
        

        if r % n == 0:
            rbefore = (r-1)//n
            ans = (rbefore-lbefore) * total
            return ans + lsum
        
        r = r + 1
        if r % n == 0:
            rbefore = (r-1)//n
            rind = n
        else:
            rbefore = r//n
            rind = r%n

        ans = (rbefore-lbefore) * total
        rshift = rbefore + 1
        rxa = (rind + rshift - 1)%n
        if rxa == 0:
            rxa = n
        endpos = n - rshift + 1

        if endpos >= rind:
            rsum = total - lookup[rxa-1] + lookup[rshift-1]
        else:
            rsum = lookup[rshift-1] - lookup[rxa-1]

        # print(rbefore, rind, rshift, rsum)
        return ans + lsum - rsum


    for _ in range(q):
        left, right = list(map(int, input().split()))
        print(compute(left, right))


