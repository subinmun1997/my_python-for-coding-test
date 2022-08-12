n, m = map(int, input().split())

result = 1
for _ in range(n):
    num = list(map(int, input().split()))
    result = max(result, min(num))

print(result)