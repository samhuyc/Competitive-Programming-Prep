

from sys import stdin, stdout
import heapq
import re
import math
from collections import deque, defaultdict, Counter


t = int(input())

def sieve_of_eratosthenes(max_num):
    is_prime = [True] * (max_num + 1)
    p = 2
    while p * p <= max_num:
        if is_prime[p]:
            for i in range(p * p, max_num + 1, p):
                is_prime[i] = False
        p += 1
    prime_numbers = [p for p in range(2, max_num + 1) if is_prime[p]]
    return set(prime_numbers)

for _ in range(t):
    n = int(input())
    primes = sieve_of_eratosthenes(n*10)
    newcolor = []
    for i in range(1, n+1):
        print(i)
        for j in range(1, i):
            if i^j in primes:
                print(i, j)
    for i in range(2, n+1):
        if (1 ^ i) in primes:
            newcolor.append(i)
    
    print(newcolor)


# def construct_graph(n, prime_numbers):
#     graph = {i: set() for i in range(1, n + 1)}
#     for u in range(1, n + 1):
#         for v in range(u + 1, n + 1):
#             if (u ^ v) in prime_numbers:
#                 graph[u].add(v)
#                 graph[v].add(u)
#     return graph

# def greedy_coloring(graph):
#     color = {}
#     for u in sorted(graph, key=lambda x: len(graph[x]), reverse=True):
#         available_colors = set(range(len(graph)))
#         for v in graph[u]:
#             if v in color:
#                 available_colors.discard(color[v])
#         color[u] = min(available_colors)
#     return color

# def color_graph(n):
#     prime_numbers = sieve_of_eratosthenes(2 * n - 1)
#     graph = construct_graph(n, prime_numbers)
#     color = greedy_coloring(graph)
#     num_colors = len(set(color.values()))
#     return color, num_colors

# # Example usage:
# n = 10
# coloring, num_colors = color_graph(n)
# print(f"Coloring: {coloring}")
# print(f"Number of colors used: {num_colors}")