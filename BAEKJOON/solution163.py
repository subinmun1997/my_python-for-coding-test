def GCD(a, b):
    while a*b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return a+b


t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    gcd = GCD(a, b)
    print((a*b)//gcd)

'''
a, b의 최소공배수 : ( a * b ) // gcd(a,b)
'''