import math

n = int(input())
factorial = str(math.factorial(n))[::-1]
for i in factorial:
    if i != '0':
        print(i)
        exit()

