from sys import stdin
from collections import Counter
def getprimes(n):
    if n <= 0:
        return []

    n = int(n)
    lst = [True for _ in range(n+1)]
    primes = []
    limit = n**0.5
    
    for i in range(2, n+1, 1):
        if lst[i] == True:
            primes.append(i)
        
            if i <= limit:
                for j in range(0, n+1, i):
                    lst[j] = False
    return primes

def getMultipliers(a):
    primes = getprimes(a)
    multipliers = []
    for val in primes:
        while a%val == 0:
            multipliers.append(val)
            a = a/val
    
    if a > 1:
        multipliers.append(a)
    return Counter(multipliers)
      
def gearnumber(a, b):
    multA, multB = getMultipliers(a), getMultipliers(b)
    result = 1
    for key, val in multA.items():
        if key in multB:
            val = max(multB[key], multA[key])
            del multB[key]
        result*= key**val
    
    for key,val in multB.items():
        result *= key**val
    
    return result


n = []
s = []
ans = 0

for line in stdin:
    curr = ""
    Number = []
    Symbol = []

    for i, char in enumerate(line):

        if char.isdigit():
            if curr == "":
                currInd = i
            curr += char

        else:
            if curr != "":
                Number.append((int(curr), currInd, i-1))
                curr = ""
            if char == "*":
                Symbol.append(i)
    
    if curr != "":
        Number.append((int(curr), currInd, i))

    n.append(Number)
    s.append(Symbol)

ans = 0
totalline = len(s)

for i, line in enumerate(s):
    for gearInd in line:
        numberMet = []
        for j in range(max(i-1,0), min(totalline, i+2)):
            for number in n[j]:
                if gearInd >= number[1]-1 and gearInd <= number[2]+1:
                    numberMet.append(number[0])
        if len(numberMet) == 2:
            ans += numberMet[0]*numberMet[1]
            #gearnumber(numberMet[0], numberMet[1])
            print(numberMet)


print(ans)

        
        






        
    
