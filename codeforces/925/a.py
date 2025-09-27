from sys import stdin
t = int(input())
for _ in range(t):
    line = int(input().strip())
    ans = ''
    if line - 3 > 25 and line -3 <= 50:
        line -= 25
        ans = "a" + chr(line-3+97) +"z"
    elif line - 3 > 50:
        ans = chr(line-53+97) + "zz"
    else:
        ans = "a" + "a" + chr(line-3+97)
    print(ans)
