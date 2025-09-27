from sys import stdin
import math

t = int("".join(input().split()[1:]))
d = int("".join(input().split()[1:]))

c = (t**2/4-d)**0.5

print(math.ceil(t/2), math.floor(c+t/2))
print(math.ceil(t/2-c), math.floor(t/2))


print(math.floor(c+t/2)-math.ceil(t/2-c)+1)
