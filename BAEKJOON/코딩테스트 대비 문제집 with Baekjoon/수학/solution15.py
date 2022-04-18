import math
from itertools import combinations

t = int(input())

for _ in range(t):
    numbers = list(map(int, input().split()))
    numbers.pop(0)
    comb = combinations(numbers, 2)

    result = 0
    for x, y in comb:
        result += math.gcd(x, y)

    print(result)