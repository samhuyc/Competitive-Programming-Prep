

def getPrimes(n):
    if n <= 0:
        return []

    limit = int(n**0.5)+1
    lst = [True for _ in range(limit)]
    primes = []
    
    for i in range(2, limit):
        if lst[i] == True:
            primes.append(i)
        
            if i <= limit:
                for j in range(0, limit, i):
                    lst[j] = False

    return primes

def getfactors(primes, n, x):
    ans = 0
    k = []
    # case 1
    
    curr = (n-x)//2
    currcopy = curr
    limit = int(curr **0.5)+1
    divisors = [1]
    for p in primes:
        if p > limit or currcopy/p + 1 < x -1:
            break
        while curr % p == 0:
            curr = curr//p
            newdiv = [p*val for val in divisors if currcopy//(p*val) + 1 >= x-1]
            divisors.extend(newdiv)
    for d in divisors:
        if currcopy//d + 1 >= x:
            k.append(currcopy//d + 1)
    # print(currcopy, k)
    # print(print(list(set(divisors))))
    # ans += len(list(set(divisors)))

    # case 2
    curr = (n+x-2)//2
    currcopy = curr
    limit = int(curr **0.5)+1
    divisors = [1]
    for p in primes:
        if p > limit or currcopy/d + 1 < x-1:
            break
        while curr % p == 0:
            curr = curr//p
            newdiv = [p*val for val in divisors if currcopy//(p*val)+1 >= x-1]
            divisors.extend(newdiv)
    # print(list(set(divisors)))
    # ans += len(list(set(divisors)))
    for d in divisors:
        if currcopy//d + 1 >= x+1:
            k.append(currcopy//d + 1)
    # print(currcopy, k)
    
    # print(list(set(k)))  
    print(len(list(set(k))))

def main():
    t = int(input())
    max_search = 0
    info = []

    for _ in range(t):
        n, x = list(map(int, input().split()))
        if (n-x) %2 == 0:
            max_search = max(max_search, (n-x)//2)
        if (n+x) %2 == 0:
            max_search = max(max_search, (n+x+2)//2)
        if (n-x) %2 != 0 and (n+x) %2 != 0:
            info.append((-1, -1))
        else:
            info.append((n, x))
        # print(n, x, max_search)
    pri = getPrimes(max_search)
    # print(pri)

    for n, x in info:
        if n == -1:
            print(0)
            continue

        getfactors(pri, n, x)

main()
