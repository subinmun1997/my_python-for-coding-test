n = int(input())

level = []
for i in range(n):
    level.append(int(input()))

level.reverse() # 5 7 3 5
cnt = 0
first = level[0]

for i in range(1, n):
    if first <= level[i]:
        tmp = level[i] - first + 1
        level[i] -= tmp
        cnt += tmp
    first = level[i]

print(cnt)