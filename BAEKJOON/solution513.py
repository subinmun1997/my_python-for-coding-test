import math

t = int(input())

for _ in range(t):
    x, y = map(int, input().split())
    print((x*y)//math.gcd(x, y), math.gcd(x, y))