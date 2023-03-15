def dfs(x, y, dsum, cnt):
    global max_value

    # 네 방향 다 체크 했으면 최대값 구하고 리턴
    if cnt == 4:
        max_value = max(max_value, dsum)
        return
    # 상하좌우 체크하면서
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 범위 내이고 방문한 적이 없는 위치라면 방문 체크
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, dsum + graph[nx][ny], cnt+1)
            visited[nx][ny] = False

# ㅏ, ㅗ, ㅜ, ㅓ 체크 함수
def exce(x, y):
    global max_value

    for i in range(4):
        temp = graph[x][y]
        # 012, 123, 230, 312만 체크 (세 방향)
        for j in range(3):
            k = (i+j)%4
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < n and 0 <= ny < m:
                temp += graph[nx][ny]

        max_value = max(max_value, temp)

# 입력 조건
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
# 방문여부 체크
visited = [[False for _ in range(m)] for _ in range(n)]

dx = [-1, 0, 1, 0] # 상하좌우 이동 방향
dy = [0, 1, 0, -1]

# 출력할 최댓값
max_value = 0

for i in range(n):
    for j in range(m):
        visited[i][j] = True # 해당 위치 방문 처리
        dfs(i, j, graph[i][j], 1)
        visited[i][j] = False # dfs 다 돌았으면 방문 처리 원래대로

        exce(i, j) # ㅏ, ㅜ, ㅓ, ㅗ 방향 체크

print(max_value)