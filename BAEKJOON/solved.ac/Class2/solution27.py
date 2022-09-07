n = int(input())

info = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    score = 1
    for j in range(n):
        if info[i][0] < info[j][0] and info[i][1] < info[j][1]:
            score += 1
    print(score, end=' ')
