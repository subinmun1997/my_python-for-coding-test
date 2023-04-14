import sys
sys.setrecursionlimit(10000)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False

    if graph[x][y] == 1:
        graph[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True
    return False

t = int(input())
for _ in range(t):
    # n=가로, m=세로, k=배추의 개수
    n, m, k = map(int, input().split())
    graph = [[0 for _ in range(m)] for _ in range(n)]

    # 배추 위치 정보 입력
    for _ in range(k):
        x, y = map(int, input().split())
        # 배추가 있으면 1로 표시
        graph[x][y] = 1

    # 배추흰지렁이 최소 마리 수
    bug = 0
    for i in range(n):
        for j in range(m):
            # 배추가 있으면 dfs 탐색
            if graph[i][j] == 1:
                dfs(i, j)
                bug += 1

    print(bug)