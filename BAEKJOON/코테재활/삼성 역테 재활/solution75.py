def dfs(x, y, dsum, cnt):
    global result

    # 4개의 칸을 다 채웠으면 최댓값 찾기
    if cnt == 4:
        result = max(result, dsum)
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 범위 내이고 방문한 적이 없는 위치라면
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, dsum + graph[nx][ny], cnt + 1)
            visited[nx][ny] = False

# ㅏ, ㅓ, ㅗ, ㅜ 체크 함수
def exce(x, y):
    global result

    for i in range(4):
        # 4가지 모음의 기준점
        temp = graph[x][y]
        for j in range(3):
            # 012,123,230,301 세방향만 체크
            k = (i+j) % 4
            nx = x + dx[k]
            ny = y + dy[k]

            # 범위 내의 위치라면
            if 0 <= nx < n and 0 <= ny < m:
                temp += graph[nx][ny]

        result = max(result, temp)

# 입력 조건
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
# 방문 여부 체크
visited = [[False for _ in range(m)] for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0
for i in range(n):
    for j in range(m):
        # 방문한 적 없는 위치라면 방문해보기
        if not visited[i][j]:
            visited[i][j] = True
            dfs(i, j, graph[i][j], 1)
            visited[i][j] = False

            # ㅏ, ㅓ, ㅗ, ㅜ 중 최댓값 찾기 위한 함수
            exce(i, j)

print(result)