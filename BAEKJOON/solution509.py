import math

def change_alpha(x):
    result = 0
    x = list(x)
    for i in range(2,-1,-1):
        result += int(ord(x[2-i]) - ord('A')) * math.pow(26, i)
    return result

n = int(input())
for _ in range(n):
    l, d = map(str, input().split('-'))
    d = int(d)
    if abs(change_alpha(l) - d) <= 100:
        print("nice")
    else:
        print("not nice")
