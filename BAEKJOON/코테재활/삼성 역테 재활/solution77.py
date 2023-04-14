n, m = map(int, input().split())
# 0=빈 칸, 1=벽, 2=바이러스
graph = [list(map(int, input().split())) for _ in range(n)]
temp_graph = [[0 for _ in range(m)] for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 바이러스 확산시키는 함수
def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if temp_graph[nx][ny] == 0:
                temp_graph[nx][ny] = 2
                virus(nx, ny)

# 안전 영역의 크기 구하는 함수
def get_score():
    cnt = 0
    for x in range(n):
        for y in range(m):
            if temp_graph[x][y] == 0:
                cnt += 1

    return cnt

result = 0
def dfs(graph, cnt):
    global result

    if cnt == 3:
        # 원래 배열 변경 막기 위해 deepcopy 방식으로 배열 값 옮기기
        for i in range(n):
            for j in range(m):
                temp_graph[i][j] = graph[i][j]

        for i in range(n):
            for j in range(m):
                # 바이러스가 있는 위치라면 확산시키기
                if temp_graph[i][j] == 2:
                    virus(i, j)

        # 안전 영역의 최대 크기 갱신
        result = max(result, get_score())
        return

    for i in range(n):
        for j in range(m):
            # 빈 칸이면 벽 세워보기
            if graph[i][j] == 0:
                graph[i][j] = 1
                dfs(graph, cnt+1)
                graph[i][j] = 0

dfs(graph, 0)
print(result)