import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
pos = sorted(list(map(int, input().split())))

if k >= n:
    print(0)
    exit()

dist = []
for i in range(1, n):
    dist.append(pos[i] - pos[i-1])

dist.sort(reverse=True)
for _ in range(k-1):
    dist.pop(0)

print(sum(dist))