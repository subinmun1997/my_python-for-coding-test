import sys
input = sys.stdin.readline

def binary(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return False

t = int(input())
for _ in range(t):
    n = int(input())
    one = sorted(list(map(int, input().split())))

    m = int(input())
    two = list(map(int, input().split()))

    for i in two:
        if binary(one, i, 0, n-1):
            print(1)
        else:
            print(0)
