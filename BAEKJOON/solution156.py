import sys

def binary_search(array, target, start, end):
    while(start <= end):
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))

c_data = sorted(list(set(data)))

for i in data:
    result = binary_search(c_data, i, 0, len(c_data)-1)
    if result != None:
        print(result, end=' ')