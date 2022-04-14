import math

t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    print(math.lcm(a, b))


'''
# 다른 방법
def gcd(a, b):
    while a*b != 0:
        if a > b:
            a = a%b
        else:
            b = b%a
    return a+b

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(a*b//gcd(a, b))
'''