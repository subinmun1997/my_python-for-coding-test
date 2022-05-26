import sys
input = sys.stdin.readline

n, m = map(int, input().split())
numbers = list(map(int, input().split()))
pre_sum = [0]

for i in range(n):
    pre_sum.append(pre_sum[-1] + numbers[i])

for _ in range(m):
    x, y = map(int, input().split())
    print(pre_sum[y] - pre_sum[x-1])
