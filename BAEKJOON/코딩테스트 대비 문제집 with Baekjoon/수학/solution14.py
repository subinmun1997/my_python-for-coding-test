import math

n = int(input())
array = list(map(int, input().split()))
x = int(input())

result = []
for i in array:
    temp = math.gcd(i, x)
    if temp == 1:
        result.append(i)

print(sum(result) / len(result))