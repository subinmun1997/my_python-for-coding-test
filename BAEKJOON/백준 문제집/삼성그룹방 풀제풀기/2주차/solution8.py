import sys
sys.setrecursionlimit(1000000)

def dfs(x, y):
    # 방문처리 해주고
    visited[x][y] = True
    # 현재 위치의 색상 저장
    cur_color = graph[x][y]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 범위 내이고
        if 0 <= nx < n and 0 <= ny < n:
            # 방문한 적 없는 칸이고
            if not visited[nx][ny]:
                # 현재 칸의 색상과 동일하다면
                if graph[nx][ny] == cur_color:
                    dfs(nx, ny)

# 입력 조건
n = int(input())
graph = [list(input()) for _ in range(n)]

# 적록색약이 아닌 사람이 봤을 때의 구역 개수
color = 0
# 적록색약인 사람이 봤을 때의 구역 개수
notcolor = 0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

visited = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        # 방문하지 않은 곳이면
        # DFS로 인접 구역 방문 처리 하고 구역 개수 하나 증가
        if not visited[i][j]:
            dfs(i, j)
            color += 1

# 적록색약은 빨간색과 초록색의 차이를 느끼지 못한다
# 초록색인 칸을 빨간색으로 변경해주기
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'

visited = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j)
            notcolor += 1

print(color, notcolor)