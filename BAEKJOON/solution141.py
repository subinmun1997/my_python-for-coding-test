n, m = map(int, input().split())
tree = list(map(int, input().split()))
tree.sort()

start = 0
end = max(tree)

result = 0
while start <= end:
    mid = (start + end) // 2
    total = 0
    for t in tree:
        if t > mid:
            total += (t-mid)
    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)
