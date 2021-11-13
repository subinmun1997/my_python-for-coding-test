import sys

n, m = map(int, sys.stdin.readline().split())
dict = {}

for _ in range(n):
    key, value = map(str, input().split())
    dict[key] = value

for i in range(m):
    data = input()
    print(dict[data])