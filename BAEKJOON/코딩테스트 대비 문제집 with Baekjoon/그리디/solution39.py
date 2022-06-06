n = int(input())
level = [int(input()) for _ in range(n)]

answer = 0
for i in range(n-2, -1, -1):
    if level[i] >= level[i+1]:
        answer += (level[i] - level[i+1] +1)
        level[i] = level[i+1] - 1

print(answer)