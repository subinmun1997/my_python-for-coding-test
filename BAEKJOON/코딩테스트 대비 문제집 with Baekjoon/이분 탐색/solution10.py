import sys
input = sys.stdin.readline

n, m = map(int, input().split())
point = sorted(list(map(int, input().split())))

def min_point(a):
    start, end = 0, n-1
    while start <= end:
        mid = (start + end) // 2

        if point[mid] < a:
            start = mid + 1
        else:
            end = mid - 1

    return end + 1

def max_point(b):
    start, end = 0, n-1
    while start <= end:
        mid = (start + end) // 2

        if b < point[mid]:
            end = mid - 1
        else:
            start = mid + 1

    return end

for _ in range(m):
    a, b = map(int, input().split())
    print(max_point(b) - min_point(a) + 1)
