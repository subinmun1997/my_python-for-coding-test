import math

t = int(input())
for _ in range(t):
    result = 0
    num = list(map(int, input().split()))
    for i in range(1, len(num)):
        for j in range(i+1, len(num)):
            result += math.gcd(num[i], num[j])

    print(result)