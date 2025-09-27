import math
import heapq
from collections import deque, defaultdict, Counter


t = int(input())

class UF():

    def __init__(self, n):
        self.p = [i for i in range(n)]
        self.rank = [1 for i in range(n)]
        self.num = n
    
    def find(self, i):
        if self.p[i] == i:
            return i
        else:
            rep = self.find(self.p[i])
            self.p[i] = rep
            return rep

    def same(self, i, j):
        return self.find(i) == self.find(j)


    def unionset(self, i, j):
        if self.same(i, j):
            return
        
        repi, repj = self.find(i), self.find(j)

        if self.rank[repi] < self.rank[repj]:
            self.p[repi] = repj
        else:
            self.p[repj] = repi

            if self.rank[repi] == self.rank[repj]:
                self.rank[repi] += 1
        
        self.num -= 1



for _ in range(t):
    n, m = list(map(int, input().split()))
    seg = {}
    for di in range(1, 11):
        seg[di] = {}
        for remain in range(di):
            seg[di][remain] = []
        

    for _ in range(m):
        a,d, k = list(map(int, input().split()))
        start, end = a, a + k * d
        remain = a % d
        seg[d][remain].append((start, end))



    uf = UF(n)
    # print(seg)
    for di in range(1, 11):
        for remain in range(di):
            curr = seg[di][remain]
            if not curr:
                continue

            curr.sort(key=lambda x:(x[0], x[1]))
            # print(curr)
            merged = []
            last_s, last_e = curr[0]

            for s, e in curr[1:]:
                if s <= last_e:
                    last_e = max(last_e, e)
                else:
                    merged.append((last_s, last_e))
                    last_s, last_e = s, e
            merged.append((last_s, last_e))

            for s, e in merged:
                for v in range(s, e+1, di):
                    uf.unionset(v-1, s-1)

    print(uf.num)

