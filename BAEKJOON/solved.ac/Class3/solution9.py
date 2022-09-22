from math import factorial

n = int(input())
fact = str(factorial(n))[::-1]

cnt = 0
for i in fact:
    if i == '0':
        cnt += 1
    else:
        break

print(cnt)