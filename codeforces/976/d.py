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
    uf = UF(n)

    seg = {}
    for di in range(1, 11):
        seg[di] = {}
        for remain in range(di):
            seg[di][remain] = []


    for info in range(m):
        a,d, k = list(map(int, input().split()))


        curr = a - 1
        for mult in range(1, k+1):
            new = curr + mult*d
            uf.unionset(curr, new)
    
    print(uf.num)
