
import math

t = int(input())


for _ in range(t):
    l, r = list(map(int, input().split()))

    print(int(math.log2(r)))
    
