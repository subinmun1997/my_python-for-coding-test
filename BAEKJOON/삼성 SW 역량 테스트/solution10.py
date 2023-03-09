import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

# 가장 처음에 양분은 모든 칸에 5만큼 들어있다.
origin_oil = [[5 for _ in range(n)] for _ in range(n)]
plus_oil = [] # 각 칸마다 추가되는 양분
for _ in range(n):
    plus_oil.append(list(map(int, input().split())))

# 심은 나무들의 정보
live = [[[] for _ in range(n)] for _ in range(n)]
for _ in range(m):
    x, y, z = map(int, input().split()) # (x, y): 위치, z: 나무의 나이
    live[x-1][y-1].append(z)

for i in range(k): # k년 반복
    for x in range(n):
        for y in range(n):
            if live[x][y]: # 해당 지점에 나무가 존재하면
                live[x][y].sort() # 여러 개의 나무가 있을 경우, 나이가 어린 나무부터 양분 섭취
                temp_live_tree = [] # 해당 지점 나무들의 새로운 나이 정보 저장
                depth = 0 # 죽은 나무들은 양분으로 변화
                for age in live[x][y]:
                    if age <= origin_oil[x][y]:
                        origin_oil[x][y] -= age
                        age += 1
                        temp_live_tree.append(age)
                    else:
                        depth += age // 2
                origin_oil[x][y] += depth # 죽어서 양분으로 변한 나무 더하기
                live[x][y] = []
                live[x][y].extend(temp_live_tree) # 해당 지점 나무들의 새로운 나이로 바꿔주기

    dx = [-1, 0, 1, 0, 1, 1, -1, -1]
    dy = [0, 1, 0, -1, 1, -1, 1, -1]
    for x in range(n):
        for y in range(n):
            if live[x][y]:
                for age in live[x][y]:
                    if age % 5 == 0: # 나무의 나이가 5의 배수라면
                        for dir in range(8):
                            nx = x + dx[dir]
                            ny = y + dy[dir]
                            if 0 <= nx < n and 0 <= ny < n:
                                live[nx][ny].append(1)

    for i in range(n):
        for j in range(n):
            origin_oil[i][j] += plus_oil[i][j]

# k년 후 땅에 살아있는 나무의 총 개수
result = 0
for i in range(n):
    for j in range(n):
        result += len(live[i][j])

print(result)