from sys import stdin

mat = None

for line in stdin:
    line = ["#"]+list(line[:-1])+["#"]   
    if mat == None:
        mat = []
        mat.append(["#" for _ in range(len(line))])
    mat.append(line)
mat.append(["#" for _ in range(len(line))])

height = len(mat)
width = len(mat[0])




    
            


    



    


    


            

            




