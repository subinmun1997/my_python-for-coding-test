from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def bfs(x, y):
    global bug

    queue = deque()
    queue.append((x, y))
    graph[x][y] = 0
    bug += 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위 내이고, 배추가 있는 칸이라면 0으로 바꾸기
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    queue.append((nx, ny))

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

    # 필요한 벌레 수
    bug = 0
    for i in range(n):
        for j in range(m):
            # 해당 위치에 배추가 있으면, 연결된 배추 0으로 바꾸고 벌레 한 마리 증가
            if graph[i][j] == 1:
                bfs(i, j)

    # 필요한 최소의 배추흰지렁이 마리 수
    print(bug)