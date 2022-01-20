import sys
input = sys.stdin.readline

n = int(input())
rank = [int(input()) for _ in range(n)]
rank.sort()

result = 0
for i in range(1, n+1):
    result += abs(i-rank[i-1])

print(result)