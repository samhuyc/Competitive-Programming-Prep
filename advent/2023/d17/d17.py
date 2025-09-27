from sys import stdin

mat = []
for line in stdin:
    line = line[:-1]
    mat.append(list(map(int, list(line))))

height = len(mat)
width = len(mat[0])
moves = [[{} for _ in range(width)]for _ in range(height)]
moves[0][0][(0,0)] = 0






