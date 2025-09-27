
info = input().split(",")

ans = 0

def hash(st):
    curr = 0
    for char in st:
        curr += ord(char)
        curr *= 17
        curr = curr % 256
    return curr



box = [[] for _ in range(256)]
box_lookup = [{} for _ in range(256)]

for task in info:
    if "=" in task:
        label, focal = task.split("=")
        boxnum = hash(label)
        focal = int(focal)

        if label in box_lookup[boxnum]:
            currind = box_lookup[boxnum][label]
            box[boxnum][currind] = [label, focal]
        else:
            box[boxnum].append([label, focal])
            box_lookup[boxnum][label] = len(box[boxnum])-1
    
    else:
        label = task[:-1]
        boxnum = hash(label)
        if label in box_lookup[boxnum]:
            currind = box_lookup[boxnum][label]
            box[boxnum].pop(currind)
            del box_lookup[boxnum][label]
            for key, loc in box_lookup[boxnum].items():
                if loc > currind:
                    box_lookup[boxnum][key] -= 1
    


ans = 0
for i, sinbox in enumerate(box):
    for ind, [name, f] in enumerate(sinbox):
        ans += (i+1)*(ind+1)*f

print(ans)







