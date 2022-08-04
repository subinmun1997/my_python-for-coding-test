n, m = map(int, input().split())
tree = sorted(list(map(int, input().split())))

start = 0
end = max(tree)

while start <= end:
    mid = (start + end) // 2

    cut = 0
    for i in tree:
        if i > mid:
            cut += i - mid

    if cut < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)