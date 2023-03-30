from collections import deque

def bfs(x, y):
    queue = deque()
    temp = [] # 연합을 이룰 수 있는 국가 담는 배열
    queue.append((x, y))
    temp.append((x, y))

    # queue에 원소가 없을 때까지
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 상하좌우 살펴보며
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 내이고 and 방문한 적이 없다면 and 새 위치와 현 위치의 인구차가 l이상 r이하라면
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                    # 방문 처리하고 큐와 temp에 담기
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
                    temp.append((nx, ny))

    return temp

# 입력 조건
n, l, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 출력 조건
result = 0
while True:
    # 각 나라 방문 여부 체크
    visited = [[0] * n for _ in range(n)]
    # while문 빠져나오기 위한 변수
    flag = 0

    # n * n 모든 나라 체크
    for i in range(n):
        for j in range(n):
            # 아직 방문하지 않았다면
            if visited[i][j] == 0:
                # 방문 처리
                visited[i][j] = 1
                # 연합을 이룰 수 있는 국가 세기
                country = bfs(i, j)
                # 국경선을 열 수 있는 나라가 1개 이상이라면
                if len(country) > 1:
                    flag = 1
                    # 각 나라의 인구수는 (연합의 인구수) / (연합을 이루고 있는 칸의 개수)
                    numbers = sum([graph[x][y] for x, y in country]) // len(country)
                    # 인구 이동
                    for x, y in country:
                        graph[x][y] = numbers

    # 국경선을 공유하는 나라가 없다면 끝내기
    if flag == 0:
        break
    result += 1

print(result)