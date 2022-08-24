n = int(input())
target = sorted(list(map(int, input().split())))
m = int(input())
arr = list(map(int, input().split()))

def binary_search(start, end, array, check):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == check:
            return 1
        elif array[mid] < check:
            start = mid + 1
        else:
            end = mid - 1
    return 0

for i in arr:
    print(binary_search(0, n-1, target, i))