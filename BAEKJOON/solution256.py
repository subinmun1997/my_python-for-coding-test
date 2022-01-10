import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    data = list(map(int, input().split()))
    data.sort(reverse=True)
    print(data[2])