n = int(input())
n_list = sorted(list(map(int, input().split())))
m = int(input())
m_list = list(map(int, input().split()))

def binary_search(start, end, arr, target):
    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            return 1
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return 0

for i in m_list:
    print(binary_search(0, n-1, n_list, i), end=' ')