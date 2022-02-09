n = int(input())
data = list(map(int, input().split()))

up = 0
answer = []
for i in range(1, n):
    if data[i] - data[i-1] > 0:
        up += data[i] - data[i-1]
    else:
        answer.append(up)
        up = 0
    answer.append(up)

print(max(answer))