'''
[접근법]
문제에서 '최소일수', '주변의 토마토들을 익힘'이라는 말이 있어서 bfs를 사용해야 한다.
깊이 들어갈 일이 없기 때문에 dfs를 사용하면 안된다.
'''

from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def bfs():
    while queue:
        # 처음 토마토 좌표 x, y에 꺼내고
        x, y = queue.popleft()
        # 처음 토마토 사분면의 익힐 토마토들을 찾아본다.
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 해당 좌표가 좌표 크기를 넘어가지 않고, 그 좌표에 익지 않은 토마토가 있다면
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                # 익히고 1을 더해주면서 횟수를 세어주기
                graph[nx][ny] = graph[x][y] + 1
                # 여기서 나온 제일 큰 값이 정답
                queue.append((nx, ny))

m, n = map(int, input().split())
# 처음 토마토 상태 입력
graph = [list(map(int, input().split())) for _ in range(n)]

queue = deque()
# queue에 처음에 받은 토마토의 위치 좌표를 append 한다
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append((i, j))

bfs()
result = 0
for i in graph:
    for j in i:
        # 완탐돌며 다 찾아봤는데 익지 않은 토마토가 있다면 -1 출력
        if j == 0:
            print(-1)
            exit()
    # 다 익혔다면 최댓값이 정답
    result = max(result, max(i))

# 처음 시작을 1로 표현했으니 1을 빼준다
print(result-1)