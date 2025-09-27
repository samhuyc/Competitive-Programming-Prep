import math
from collections import deque, defaultdict, Counter



t = int(input())


for _ in range(t):

    x = int(input())
    bi = list(bin(x)[2:])

    flag = True
    while flag:
        flag = False
        for i in range(len(bi)-1):
            fir, sec = bi[i], bi[i+1]
            if fir != "0" and sec != "0":
                flag = True
                if fir == "1" and sec == "1":
                    if i != 0:
                        bi = bi[:i-1] + ["1", "0", "-1"] + bi[i+2:]
                    else:
                        bi = bi[:i] + ["1", "0", "-1"] + bi[i+2:]
                elif fir == "1" and sec == "-1":
                    bi = bi[:i] + ["0", "1"] + bi[i+2:]
                elif fir == "-1" and sec == "1":
                    bi = bi[:i] + ["0", "-1"] + bi[i+2:]
                else:
                    if i != 0:
                        bi = bi[:i-1] + ["-1", "0", "1"] + bi[i+2:]
                    else:
                        bi = bi[:i] + ["-1", "0", "1"] + bi[i+2:]

    c = deque()
    for v in bi:
        c.appendleft(v)
    print(len(c))
    print(" ".join(c))