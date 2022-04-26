import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline
n, m = map(int, input().split())
point = sorted(list(map(int, input().split())))
line = []

for _ in range(m):
    x, y = map(int, input().split())
    line.append((x, y))

for x, y in line:
    left = bisect_left(point, x)
    right = bisect_right(point, y)
    print(right - left)
