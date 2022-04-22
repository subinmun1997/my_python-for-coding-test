k, n = map(int, input().split())
array = sorted([int(input()) for _ in range(k)])

start = 1
end = max(array)

result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for i in array:
        total += i // mid
    if total < n:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)
