

from sys import stdin, stdout
import heapq
import re
import math
from collections import deque, defaultdict, Counter




def sieve_of_eratosthenes(max_num):
    is_prime = [True] * (max_num + 1)
    p = 2
    while p * p <= max_num:
        if is_prime[p]:
            for i in range(p * p, max_num + 1, p):
                is_prime[i] = False
        p += 1
    is_prime[0] = False
    is_prime[1] = False
    return is_prime

t = int(input())
primes = sieve_of_eratosthenes(2*10**5)


for _ in range(t):
    n = int(input())
    color = [0] * (n+1)

    for i in range(1, n+1):
        if color[i] == 0:
            color[i] = 1
            for j in range(1, n+1):
                if i!= j and primes[i^j]:
                    if color[j] == 0:
                        color[j] = 2

    print(color[1:])
    

            






