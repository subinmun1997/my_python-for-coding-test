import math

n = int(input())
p = list(map(int, input().split()))
a, b = map(int, input().split())

result = n
for i in p:
    if i <= a:
        continue
    else:
        result += math.ceil((i-a)/b)

print(result)