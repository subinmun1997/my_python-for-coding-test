def GCD(a, b):
    while a*b != 0:
        if a>b:
            a %= b
        else:
            b %= a
    return a+b

n, m = map(int, input().split())
gcd = GCD(n,m)
print(gcd)
print((m*n) // gcd)