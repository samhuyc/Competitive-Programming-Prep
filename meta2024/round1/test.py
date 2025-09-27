import math
from itertools import combinations, permutations, product

def solve():
    n = int(input())
    st = [[ord(v)- 65 if v != "?" else -1 for v in list(input())] for _ in range(n)]
    maxlen = max([len(s) for s in st])
    res = 1
    for s in st:
        curr = 1
        for char in s:
            if char != -1:
                res += curr
            else:
                curr *= 26
                res += curr
        print(res)
    
    sign = 1
    for k in range(2, n+1):
        sign *= -1
        possibility = list(combinations(range(n), k))
        for selected in possibility:
            selected = list(selected)
            curr = 1

            for charind in range(maxlen):
                chosen = None
                good = True
                allnum = False

                for stringind in selected:
                    if charind >= len(st[stringind]):
                        good = False
                        break

                    if st[stringind][charind] == -1:
                        continue
                    else:
                        allnum = True
                        if chosen == None:
                            chosen = st[stringind][charind]
                        else:
                            if chosen != st[stringind][charind]:
                                good = False
                                break
                
                if good and allnum:
                    curr *= 1
                    res += sign * curr 
                elif good and not allnum:
                    curr *= 26
                    res += sign * curr
                else:
                    break
    return res


def main():
    t = int(input())

    for case in range(t):
        ans = solve()
        print(f"Case #{case+1}: {ans}")

main()