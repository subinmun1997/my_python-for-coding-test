from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
temp = [[0 for _ in range(m)] for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 바이러스 확산시키는 함수
def virus(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위 내이고, 빈 칸이라면 바이러스 확산시키기
            if 0 <= nx < n and 0 <= ny < m and temp[nx][ny] == 0:
                temp[nx][ny] = 2
                queue.append((nx, ny))

# 안전 영역의 크기 구하는 함수
def get_score():
    cnt = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                cnt += 1

    return cnt

result = 0
def make_wall(cnt):
    global result

    if cnt == 3:
        for i in range(n):
            for j in range(m):
                # deepcopy 용도
                temp[i][j] = graph[i][j]

        for i in range(n):
            for j in range(m):
                # 바이러스가 있으면 확산시키기
                if temp[i][j] == 2:
                    virus(i, j)

        result = max(result, get_score())
        return

    for i in range(n):
        for j in range(m):
            # 빈 칸이면 벽 세워보기
            if graph[i][j] == 0:
                graph[i][j] = 1
                make_wall(cnt + 1)
                graph[i][j] = 0

make_wall(0)
print(result)