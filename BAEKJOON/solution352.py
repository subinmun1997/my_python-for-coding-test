n = int(input())
room = [input() for _ in range(n)]
x = y = 0 # x: 가로 y: 세로

for i in range(n):
    check = 0
    for j in range(n):
        if room[i][j] == '.':
            check += 1
        else:
            check = 0
        if check == 2:
            x += 1
for i in range(n):
    check = 0
    for j in range(n):
        if room[j][i] == '.':
            check += 1
        else:
            check = 0
        if check == 2:
            y += 1

print(x, y)

