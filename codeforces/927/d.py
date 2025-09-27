from collections import deque, defaultdict


t = int(input())

for _ in range(t):
    n = int(input())
    tc  = input()
    info = input().split()
    dic = defaultdict(list)

    for val in info:
        if val[-1] == tc:
            dic['T'].append(int(val[0]))
        else:
            dic[val[-1]].append(int(val[0]))
    
    trump = dic['T']
    trump.sort()
    del dic['T']

    ans = []
    wrong = 0
    for suit, lst in dic.items():
        lst.sort()
        if len(lst) %2 == 0:
            while lst:
                a = lst.pop()
                b = lst.pop()
                ans.append((str(b)+suit, str(a)+suit))
        else:
            if trump:
                t = trump.pop(0)
                a = lst.pop()
                ans.append((str(a)+suit, str(t)+tc))
                while lst:
                    a = lst.pop()
                    b = lst.pop()
                    ans.append((str(b)+suit, str(a)+suit))
            else:
                wrong = 1
                break
    
    if len(trump)%2 != 0:
        wrong = 1
    else:
        while trump:
            a = trump.pop()
            b = trump.pop()
            ans.append((str(b)+tc, str(a)+tc))

    if wrong:
        print('IMPOSSIBLE')
    else:
        for first, second in ans:
            print(f"{first} {second}")


