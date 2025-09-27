from sys import stdin
from itertools import combinations

def check(dloc, condition, info):
    currcond = condition.copy()
    currinfo = []
    
    tally = 0 
    for i, char in enumerate(currcond):
        if i in dloc:
            char = "#"
        else:
            if char == "?":
                char = "."
        
        if char == "#":
            tally += 1
        else:
            if tally == 0:
                continue

            if info[len(currinfo)] != tally:
                return False
            else:
                currinfo.append(tally)
                tally = 0
        
    if tally != 0:
        if info[len(currinfo)] != tally:
            return False

        else:
            return True
    

ans = 0
for line in stdin:
    condition, info = line.split()
    condition = list(condition)
    info = list(map(int, info.split(",")))

    condition = condition 
    info = info 

    unknownind = []
    for i, char in enumerate(condition):
        if char == "?":
            unknownind.append(i)
    
    currd = condition.count("#")
    actuald = sum(info)
    setd = actuald-currd

    c = combinations(unknownind, setd)
    for dloc in c:
        if check(list(dloc), condition, info):
            ans += 1

            

print(ans)



