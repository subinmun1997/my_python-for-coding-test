def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return True
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return False

n = int(input())
cards = sorted(list(map(int, input().split())))
m = int(input())
check = list(map(int, input().split()))

for i in check:
    if binary_search(cards, i, 0, n-1):
        print(1, end=' ')
    else:
        print(0, end=' ')
