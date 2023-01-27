n = input()

minvalue = 1e9
maxvalue = 0

def countOdd(n):
    oddNum = 0
    for i in n:
        if int(i)%2 != 0:
            oddNum += 1
    return oddNum

def solve(n, oddNum):
    global minvalue, maxvalue

    if len(n) == 1:
        minvalue = min(minvalue, oddNum)
        maxvalue = max(maxvalue, oddNum)
    elif len(n) == 2:
        temp = str(int(n[0]) + int(n[1]))
        solve(temp, oddNum + countOdd(temp))
    else:
        for i in range(len(n)-2):
            for j in range(i+1, len(n)-1):
                a, b, c = n[:i+1], n[i+1:j+1], n[j+1:]
                temp = str(int(a) + int(b) + int(c))
                solve(temp, oddNum + countOdd(temp))

solve(n, countOdd(n))
print(minvalue, maxvalue)