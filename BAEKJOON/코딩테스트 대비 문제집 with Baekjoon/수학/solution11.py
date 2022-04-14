import math

n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    print(math.lcm(a, b))


'''
def gcd(a, b):
    while a*b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return a+b

n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    print(a*b//gcd(a, b))
'''
