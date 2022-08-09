k, n = map(int, input().split())
lan = sorted([int(input()) for _ in range(k)])

start = 1
end = max(lan)
while start <= end:
    mid = (start + end) // 2
    count = 0

    for i in lan:
        count += i // mid

    if count < n:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)