def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    cnt = 0
    for i in range(len(array)):
        if array[i] > mid:
            cnt += (array[i] - mid)
    if cnt == target:
        return mid
    elif cnt > target:
        return binary_search(array, target, mid+1, end)
    else:
        return binary_search(array, target, start, mid-1)

n, m = map(int, input().split())
t = list(map(int, input().split()))
t.sort()

result = binary_search(t, m, 0, max(t))
if result != None:
    print(result)
