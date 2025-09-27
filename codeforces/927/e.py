t = int(input())

for _ in range(t):
    n = int(input())
    
    valint = list(map(int, list(input().lstrip("0"))))
    valint = valint[::-1]
    ans = valint.copy()

    for i, v in enumerate(valint):
        currdigit = 0
        carry = 0
        for j in range(i):
            ans[j] += v + carry
            carry = 0
            currdigit = j
            if ans[currdigit] >= 10:
                ans[currdigit] -= 10
                carry += 1
                currdigit += 1
                if currdigit >= len(ans):
                    ans.append(0)
                while carry != 0:
                    ans[currdigit] += carry
                    carry = 0
                    if ans[currdigit] >= 10:
                        ans[currdigit] -= 10
                        carry += 1
                    else:
                        carry = 0
                    currdigit += 1
                    if currdigit >= len(ans):
                        ans.append(0)
    
    result = "".join(list(map(str, ans[::-1])))
    print(result.lstrip("0"))
            

            
    

    

    




        