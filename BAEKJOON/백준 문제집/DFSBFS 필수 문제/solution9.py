'''
지나야 하는 최소의 칸 수 -> bfs
'''

from collections import deque

# 입력 조건
n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위 내이고 해당 위치가 이동할 수 있는 칸이라면(1), 전 위치 + 1 한 값을 대입하기
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx, ny))

    # (n, m) 위치 값 반환
    return graph[n-1][m-1]

print(bfs(0, 0))