


from sys import stdin


def check(info):
        
    direction = None
    if info[0] < info[1]:
        direction = 1
    elif info[0] > info[1]:
        direction = -1
    else:
        return False

    good = True
    for i in range(len(info)-1):
        if direction == 1 and 1 <= info[i+1] - info[i] <= 3:
            continue
        elif direction == -1 and 1 <= info[i] - info[i+1] <= 3:
            continue
        else:
            good = False
    
    return good


ans = 0
for line in stdin:
    info = list(map(int, line.split()))

    ans += any([check(info[:i]+info[i+1:]) for i in range(len(info))])

    

print(ans)