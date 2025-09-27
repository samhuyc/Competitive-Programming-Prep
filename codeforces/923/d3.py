from collections import defaultdict
from sys import stdin


def main():
    t = int(input())

    for _ in range(t):
        nlen = int(stdin.readline())
        vals = list(map(int, stdin.readline().split()))

        threshold = [nlen+1 for _ in range(nlen)]
        
        curr = 0
        for i in range(1, nlen):
            if vals[i] != vals[i-1]:
                for j in range(curr, i):
                    threshold[j] = i
                curr = i
        
        # print(threshold)

    
        g = int(input())

        for i in range(g):
            l, r = list(map(int, stdin.readline().split()))
            l = l-1
            r = r-1
            if threshold[l] > r:
                print("-1 -1")
            else:
                print(f'{threshold[l]} {threshold[l]+1}')

main()


