t = int(input())

def gcd(a, b):
    while a*b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return a+b

for _ in range(t):
    numbers = list(map(int, input().split()))

    result = 0
    for i in range(1, len(numbers)):
        for j in range(i+1, len(numbers)):
            result += gcd(numbers[i], numbers[j])

    print(result)