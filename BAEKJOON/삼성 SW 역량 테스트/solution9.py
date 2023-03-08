from collections import deque
import sys
input = sys.stdin.readline

n, l, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0] # 상 하 좌 우 살펴보기 위한 방향 설정
dy = [0, 1, 0, -1]

def bfs(x, y):
    queue = deque()
    temp = []
    queue.append((x, y))
    temp.append((x, y))

    while queue: # queue가 없을 때까지
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 4방향을 돌면서, nx ny가 범위 내이고 방문한 적이 없다면
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                # 그리고 두 나라의 인구 차이가 L명 이상, R명 이하라면
                if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                    visited[nx][ny] = 1 # 방문 처리
                    queue.append((nx, ny)) # 새로운 연합을 찾기 위해
                    temp.append((nx, ny)) # 해당 nx, ny는 연합

    return temp

result = 0 # 인구 이동이 일어나는 총 일 수
while True:
    visited = [[0] * n for _ in range(n)] # 방문 여부 배열
    flag = 0 # while문 빠져나가기 위한 조건
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0: # 방문 안 한 곳이 있다면
                visited[i][j] = 1 # 방문처리 하고
                country = bfs(i, j) # 몇개국과 국경선 공유가 가능한지 체크

                if len(country) > 1: #국경선 공유가 가능한 나라가 2개 이상이라면
                    flag = 1
                    # 각 인구수는 (연합의 인구수) / (연합을 이루고 있는 칸의 개수)
                    number = sum([graph[x][y] for x, y in country]) // len(country)

                    # 인구 이동
                    for x, y in country:
                        graph[x][y] = number

    if flag == 0: # 국경선 공유가 가능한 나라가 더이상 없다면 빠져나가기
        break
    result += 1

print(result)