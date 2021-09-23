n, k = map(int, input().split())

array = []
for i in range(n):
    array.append(int(input()))

result = 0
array = sorted(array, reverse=True)

for i in array:
    if i <= k and k != 0:
        result += k // i
        k %= i

print(result)