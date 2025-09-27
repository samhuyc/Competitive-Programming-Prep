


from sys import stdin

mat = []
for line in stdin:
    mat.append(list(line))

count = 0
target = ['X',"M",'A','S']
for y in range(len(mat)):
    for x in range(len(mat[0])):
        if mat[y][x] == "A" and (1 <= y < len(mat)-1) and (1 <= x < len(mat[0])-1):
            if [mat[y-offset][x-offset] for offset in range(-1, 2)] in [['M','A','S'], ['S','A','M']]:
                if [mat[y+offset][x-offset] for offset in range(-1, 2)] in [['M','A','S'], ['S','A','M']]:
                    count += 1
print(count)