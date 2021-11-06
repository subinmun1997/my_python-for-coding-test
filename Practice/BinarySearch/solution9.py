def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        total = 0
        for i in array:
            if i > mid:
                total += (i - mid)
        if total == target:
            return mid
        elif total > target:
            start = mid + 1
        else:
            end = mid - 1
    return None

n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
result = binary_search(data, m, 0, max(data))
print(result)