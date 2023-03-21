def GCD(n, m):
    while n * m != 0:
        if n > m:
            n %= m
        else:
            m %= n
    return m + n

def solution(n, m):
    gcd = GCD(n, m)
    return [gcd, (n * m) // gcd]

print(solution(3, 12))
print(solution(2, 5))

