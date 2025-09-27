



def single(n):
    ans = []
    for i in range(1, 7):
        diff = i
        leftside = int(str(n)*diff) - diff
        # print(leftside)
        if leftside % (n-1) == 0:
            a = leftside//(n-1)
            b = a - diff
            if a > b and 0 < a <= 10000 and 0<b <= 10000:
                ans.append((a, b))

    return ans

def double(n):
    ans = []
    for i in range(1, 10):
        diff = i
        leftside = int((str(n)*diff)[:diff]) - diff
        # print(int((str(n)*diff)[:diff]), i)
        if leftside % (n-2) == 0:
            a = leftside//(n-2)
            b = a * 2 - diff
            if 2*a > b and 0 < a <= 10000 and 0< b <= 10000:
                ans.append((a, b))
    
    return ans



t = int(input())

for _ in range(t):
    n = int(input())
    if n == 1:
        alst = [a for a in range(2, 10001)]
        print(len(alst))
        for a in alst:
            print(str(a) + " " + str(a-1))
        continue

    if n < 10:
        ans = single(n)
    else:
        ans = double(n)
    
    print(len(ans))
    for a,b in ans:
        print(str(a) + " "+ str(b))


