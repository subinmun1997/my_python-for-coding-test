n = int(input())

file = [input() for _ in range(n)]
answer = list(file[0])

for i in range(1, n):
    for j in range(len(file[i])):
        if answer[j] != file[i][j]:
            answer[j] = '?'

print(''.join(answer))
