import math

n, m = map(int, input().split())

gcd = math.gcd(n, m)
lcm = math.lcm(n, m)
print(gcd)
print(lcm)
