n, m = map(int, input().split())

result = 0
for i in range(n):
    data = list(map(int, input().split()))
    min_value = 10001

    for a in data:
        min_value = min(min_value, a)

    result = max(min_value, result)

print(result)