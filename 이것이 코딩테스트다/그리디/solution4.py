n, m = map(int, input().split()) # 행 열

max_number = 0
for _ in range(n):
    numbers = list(map(int, input().split()))
    min_number = min(numbers) # 가장 작은 값들 중
    max_number = max(min_number, max_number) # 그 중 큰 값

print(max_number)