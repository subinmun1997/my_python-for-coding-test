def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        total = 0
        for i in array:
            if i > mid:
                total += (i - mid)
        if total < m:
            end = mid - 1
        else:
            result = mid
            start = mid + 1
    return result

n, m = map(int, input().split())
height = sorted(list(map(int, input().split())))
result = binary_search(height, m, 0, max(height))
print(result)
