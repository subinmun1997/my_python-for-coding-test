from collections import deque

# 모든 토마토가 다 익었는지 확인하는 함수
def all_tomato():
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                return False
    return True

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위 내이고, 익지 않은 토마토가 있는 칸이라면
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0:
                    # 전 칸보다 1만큼의 시간이 더 걸린다
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx, ny))

# n=가로 칸 수, m=세로 칸 수
m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 토마토가 있는 위치 저장
queue = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append((i, j))

bfs()
# 모든 토마토가 다 익었으면
# 최소 날짜 출력
if all_tomato():
    result = 0
    for i in range(n):
        result = max(result, max(graph[i]))
    # 1부터 시작했으니까 result-1이 정답
    print(result - 1)
# 토마토가 모두 익지는 못하는 상황이라면
# -1 출력
else:
    print(-1)