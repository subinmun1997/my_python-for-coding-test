n, m = map(int, input().split())

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

temp = 10001
for i in array:
    min_value = min(i)
    temp = min(temp, min_value)

print(max(min_value, temp))
