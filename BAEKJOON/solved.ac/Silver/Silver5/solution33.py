import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a = sorted(list(map(int, input().split())))
print(a[k-1])