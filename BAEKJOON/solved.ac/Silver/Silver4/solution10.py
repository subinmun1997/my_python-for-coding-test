n = int(input())
n_list = sorted(list(map(int, input().split())))
m = int(input())
m_list = list(map(int, input().split()))

def binary_search(start, end, lst, x):
    while start <= end:
        mid = (start + end) // 2
        if x == lst[mid]:
            return 1
        elif x < lst[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return 0

for i in m_list:
    print(binary_search(0, len(n_list)-1, n_list, i))