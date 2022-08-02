n, m = map(int, input().split())
numbers = list(map(int, input().split()))

count = 0
end = 0
interval_sum = 0

for start in range(n):
    while interval_sum < m and end < n:
        interval_sum += numbers[end]
        end += 1
    if interval_sum == m:
        count += 1
    interval_sum -= numbers[start]

print(count)