import math

n, m = map(int, input().split(':'))
gcd = math.gcd(n, m)

print("%d:%d" %(n//gcd, m//gcd))