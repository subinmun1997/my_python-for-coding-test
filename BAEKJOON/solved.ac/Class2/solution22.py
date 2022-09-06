n, m = map(int, input().split())
tree = sorted(list(map(int, input().split())))

start = 0
end = max(tree)

while start <= end:
    mid = (start + end) // 2
    piece = 0
    for i in tree:
        if mid < i:
            piece += i - mid

    if piece < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)