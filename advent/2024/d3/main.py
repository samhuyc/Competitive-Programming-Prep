


from sys import stdin


ans = 0
cont = 1

for line in stdin:
    
    for i in range(len(line)):
        
        if line[i] == ")" and i >= 6 and line[i-6:i+1] == "don't()":
            cont = -1
        elif line[i] == ")" and i >= 3 and line[i-3:i+1] == "do()":
            cont = 1

        if cont == 1 and line[i] == "(":
            if i < 3:
                continue
            if line[i-3:i] != "mul":
                continue
            
            seen = 0
            good = True
            st = ""
            for j in range(i+1, i+9):
                if j >= len(line):
                    good = False
                    break
                
                if line[j] == ")":
                    break

                if not (line[j].isnumeric() or line[j] == ","):
                    good = False
                    break


                if line[j] == ",":
                    seen += 1
                    if seen > 1:
                        good = False
                        break
                    else:
                        st += line[j]
                else:
                    st += line[j]
        
            if good and seen == 1:
                a, b = list(map(int, st.split(',')))
                ans += a * b




print(ans)