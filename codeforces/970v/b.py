

t = int(input())

for _ in range(t):
    n = int(input())
    st = input()
    old = st

    h = 2
    w = 0
    stop = False
    vis = False

    st = st.split("1")

    for char in st:
        if char != "":
            w = len(char)+2
            h += 1
    
    if w == 0 and h == 2:
        if len(old) == 1 or len(old) == 4:
            print("Yes")
        else:
            print("No")
        continue
    
    if w == h:
        print("Yes")
    else:
        print("No")
