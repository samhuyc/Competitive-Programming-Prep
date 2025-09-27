from collections import defaultdict
from sys import stdin


def main():
    t = int(stdin.readline())

    for _ in range(t):
        solution = []
        nlen = int(stdin.readline())
        vals2 = list(map(int, stdin.readline().split()))
        vals = [(v, -1, nlen) for v in vals2]
        lastleft = defaultdict(lambda:-1)
        lastright = defaultdict(lambda:nlen)

        for i, (v, l, r) in enumerate(vals):
            vals[i], lastleft[v] = (v, lastleft[v], r), i
            # if v in lastleft:
            #     vals[i] = (v, lastleft[v], r)
            # lastleft[v] = i
        
        for j in range(nlen-1, -1, -1):
            (v, l, r) = vals[j]
            vals[j], lastright[v] = (v, l, lastright[v]), j
            # if v in lastright:
            #     vals[j] = (v, l, lastright[v])
            # lastright[v] = j

        q = int(stdin.readline())
        for _ in range(q):
            done = 0
            l, r = list(map(int, stdin.readline().split()))
            for (prevl, prevr), (ans1, ans2) in solution:
                if prevl >= l and prevr <= r:
                    print(f"{ans1} {ans2}")
                    done = 1
            if done == 1:
                continue

            l = l-1
            r = r-1
            unique = None
            first = None
            ans = [None, None]

            for ind in range(l, r+1):
                (v, myl, myr) = vals[ind]
                if myl < l and myr > r:
                    if first == None:
                        first = v
                        unique = v
                        ans[0] = ind
                    else:
                        ans[1] = ind
                        break

                elif myl < l or myr > r:
                    if unique != None:
                        ans[1] = ind
                        break
                    else:
                        if first != None:
                            if first != v:
                                ans[1] = ind
                                break
                        else:
                            first = v
                            ans[0] = ind
            
            if ans[1] == None:
                solution.append(((l+1, r+1),(-1, -1)))
                print('-1 -1')
            else:
                solution.append(((l+1, r+1),(ans[0]+1, ans[1]+1)))
                print(f'{ans[0]+1} {ans[1]+1}')
main()