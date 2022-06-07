n = int(input())
pos = [list(map(int, input().split())) for _ in range(n)]

lst = sorted(pos, key=lambda x:x[0])
x = lst[int(n/2)][0]
lst = sorted(pos, key=lambda x:x[1])
y = lst[int(n/2)][1]

answer = 0
for i in range(n):
    answer += abs(x-pos[i][0]) + abs(y-pos[i][1])

print(answer)