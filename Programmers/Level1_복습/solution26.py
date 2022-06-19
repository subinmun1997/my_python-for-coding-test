def solution(n, m):
    return [gcd(n, m), n*m // gcd(n,m)]

def gcd(n, m):
    while n*m != 0:
        if n > m:
            n %= m
        else:
            m %= n
    return n+m

print(solution(3, 12))
print(solution(2, 5))