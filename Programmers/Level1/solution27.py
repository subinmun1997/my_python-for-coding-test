def solution(n, m):
    array = []
    array.append(gcd(n, m))
    array.append(n*m // gcd(n, m))
    return array

def gcd(a, b):
    while a*b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return a+b

print(solution(3, 12))
print(solution(2, 5))