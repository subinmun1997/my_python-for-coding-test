n = int(input())
data = list(map(int, input().split()))

cnt = 0
for i in range(n):
    if data[i] != i+1:
        cnt += 1

print(cnt)