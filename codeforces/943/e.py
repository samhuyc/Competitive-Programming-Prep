



t = int(input())


for _ in range(t):
    n = int(input())
    ans = []
    ans.append((1, 1))
    ans.append((n, n))

    total = 2
    oddcurr = (1,1)
    oddpos = "top"
    evencurr = (n, n)
    for i in range(1, n-total+1):
        if i%2 == 0:
            ans.append((evencurr[0]-1, evencurr[1]-1))
            evencurr =(evencurr[0]-1, evencurr[1]-1)
        else:
            if oddpos == "top":
                oddfirst = 1
                oddsecond = oddcurr[0]+1
                ans.append((oddfirst, oddsecond))
                oddcurr = (oddfirst, oddsecond)
                oddpos = 'side'
            else:
                oddsecond = 1
                oddfirst = oddcurr[1] + 1
                ans.append((oddfirst, oddsecond))
                oddcurr = (oddfirst, oddsecond)
                oddpos = 'top'
    for f, s in ans:
        print(f"{f} {s}")

