def gcd(x, y):
    while x * y != 0:
        if x > y:
            x %= y
        else:
            y %= x
    return x+y

n, m = map(int, input().split())
print(gcd(n, m))
print((n * m) // gcd(n, m))