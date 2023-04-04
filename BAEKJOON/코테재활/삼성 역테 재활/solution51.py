def solve(x, y, d1, d2):
    temp = [[0] * (n+1) for _ in range(n+1)]
    temp[x][y] = 5
    # 조건2
    for i in range(1, d1+1):
        temp[x+i][y-i] = 5
    for i in range(1, d2+1):
        temp[x+i][y+i] = 5
    for i in range(1, d2+1):
        temp[x+d1+i][y-d1+i] = 5
    for i in range(1, d1+1):
        temp[x+d2+i][y+d2-i] = 5

    people = [0] * 5
    # 1번 선거구
    for r in range(1, x+d1):
        for c in range(1, y+1):
            if temp[r][c] == 5:
                break
            else:
                people[0] += graph[r][c]

    for r in range(1, x+d2+1):
        for c in range(n, y, -1):
            if temp[r][c] == 5:
                break
            else:
                people[1] += graph[r][c]

    for r in range(x+d1, n+1):
        for c in range(1, y-d1+d2):
            if temp[r][c] == 5:
                break
            else:
                people[2] += graph[r][c]

    for r in range(x+d2+1, n+1):
        for c in range(n, y-d1+d2-1, -1):
            if temp[r][c] == 5:
                break
            else:
                people[3] += graph[r][c]

    people[4] = total - sum(people)
    return max(people) - min(people)

n = int(input())
graph = [[0] * (n+1)] + [[0] + list(map(int, input().split())) for _ in range(n)]

total = 0
for i in range(1, n+1):
    total += sum(graph[i])

result = int(1e9)
for x in range(1, n+1):
    for y in range(1, n+1):
        for d1 in range(1, n+1):
            for d2 in range(1, n+1):
                if x + d1 + d2 > n:
                    continue
                if y - d1 < 1:
                    continue
                if y + d2 > n:
                    continue
                result = min(result, solve(x, y, d1, d2))

print(result)