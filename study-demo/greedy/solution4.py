n, m = map(int, input().split()) # 핼 열

max_value = 0
for _ in range(n):
    data = min(list(map(int, input().split())))
    max_value = max(max_value, data)

print(max_value)