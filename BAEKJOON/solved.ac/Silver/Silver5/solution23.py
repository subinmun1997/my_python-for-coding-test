import math

n = int(input())
num = str(math.factorial(n))[::-1]

count = 0
for i in num:
    if i == '0':
        count += 1
    else:
        break
print(count)