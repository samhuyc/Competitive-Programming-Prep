from sys import stdin

ans = 0

for line in stdin:
    subgames = line.split(";")
    num = int(subgames[0].split(":")[0].split()[-1])
    alter = subgames[0].split(":")[-1]
    subgames[0] = alter

    dic = {"red": 0, 
            "green": 0, 
            "blue":0}

    for i, unit in enumerate(subgames):
        colors = unit.split(",")
        for color in colors:
            val, c = color.split()
            if int(val) > dic[c]:
                dic[c] = int(val)
    
    ans += dic["red"]*dic["green"]*dic["blue"]

print(ans)





            
        

