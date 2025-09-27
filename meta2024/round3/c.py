

import heapq
import math
import re
from itertools import combinations, permutations, product, combinations_with_replacement
from collections import deque, defaultdict,Counter
from sympy import harmonic



def solve():
    ans = 0
    N, P = list(map(int, input().split()))
    if P == 0:
        ans = float(N*(harmonic(N)))
        return ans
    


    D_lst = [i for i in range(1, math.ceil(100/P) + 2)]
    switch = []
    for ind in range(len(D_lst)-1):
        D1 = D_lst[ind]
        D2 = D_lst[ind+1]
        P1 = min((D1-1)*P, 100)
        P2 = min((D2-1)*P, 100)

        l, r = 0, N-1
        while l<= r:
            mid = (l+r)//2
            C1 = 100*D1/(P1 + (100-P1)*(N-mid)/N)
            C2 = 100*D2/(P2 + (100-P2)*(N-mid)/N)
            if C1 > C2:
                r = mid - 1
            else:
                l = mid + 1
        
        switch.append(l)

    switch.append(N)
    

    # print(D_lst)
    print(switch)

    changecount = []
    changeD = []

    last = switch[0]
    lastD = 1

    for i in range(len(switch)):
        if last != switch[i]:
            changecount.append(last)
            changeD.append(lastD)
            lastD = D_lst[i]
            last = switch[i]
    
    if not changeD or lastD != changeD[-1]:
        changeD.append(lastD)
        changecount.append(last)

    ans = 0

    if N>= 10**9:
        for ind in range(len(changeD)):
            D, til = changeD[ind], changecount[ind]
            P = min((D - 1) * P, 100)
            if P == 0 or P == 100:
                ans += 0
            else:
                denominator = 100 - P
                temp1 = 100 - (100 - P) * (til / N)
                temp2 = P
                ans2 = (100 * D * N / denominator) * (math.log(temp1) - math.log(temp2))
                ans += ans2

    else:
        prev = 0
        for ind in range(len(changeD)):
            D, til = changeD[ind], changecount[ind]
            for i in range(prev, til):
                P1 = 0
                C1 = 100*D/(P1 + (100-P1)*(N-i)/N)
                ans += C1
            prev = til
    return ans



def main():
    t = int(input())
    for case in range(t):
        ans = solve()
        print(f"Case #{case+1}: {ans}")

main()