n, m = map(int, input().split())

min_value = 0
for _ in range(n):
    data = list(map(int, input().split()))
    min_value = max(min_value, min(data))

print(min_value)
