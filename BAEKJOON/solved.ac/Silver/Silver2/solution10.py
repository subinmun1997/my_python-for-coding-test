def binary(start, end, arr, target):
    while start <= end:
        mid = (start + end) // 2

        cut = 0
        for i in arr:
            if i > mid:
                cut += (i - mid)

        if cut == target:
            return mid
        elif cut < target:
            end = mid - 1
        elif cut > target:
            answer = mid
            start = mid + 1

    return answer

n, m = map(int, input().split())
tree = sorted(list(map(int, input().split())))
result = binary(0, max(tree), tree, m)
print(result)