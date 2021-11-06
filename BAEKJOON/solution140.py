def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)

n = int(input())
array = set(map(int, input().split()))
array.sort()
m = int(input())
data = list(map(int, input().split()))

for i in data:
    if i in array:
        print(1)
    else:
        print(0)