from collections import deque

def bfs(spread_time):
    global result

    infect, times = 0, 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위를 벗어나면 넘어가기
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            # 벽이 아니고 해당 위치에 처음 도착했다면
            if graph[nx][ny] != 1 and spread_time[nx][ny] == -1:
                queue.append((nx, ny))
                # 직전 위치보다 1초 더 걸리는 위치이다
                spread_time[nx][ny] = spread_time[x][y] + 1
                # 해당 위치가 만약 빈 칸이라면
                if graph[nx][ny] == 0:
                    infect += 1 # 감염시킨 칸 하나 증가
                    times = spread_time[nx][ny]

    # 감염시킨 빈 칸의 수 == 최초 빈 칸의 수 라면 최소 시간 구해서 리턴
    if infect == no_wall:
        result = min(result, times)

def select_virus(idx, cnt, v): #인덱스, 놓은 바이러스 개수, 총 바이러스의 개수
    # m개의 바이러스를 다 놓았다면
    if cnt == m:
        # 바이러스가 해당 칸에 퍼질 때 까지의 걸린 시간 저장
        spread_time = [[-1 for _ in range(n)] for _ in range(n)]
        for i in range(v):
            if selected[i]:
                x, y = virus[i]
                queue.append((x, y))
                # 해당 위치는 바이러스니까 0으로 저장
                spread_time[x][y] = 0

        bfs(spread_time)
        return

    for i in range(idx, v):
        if not selected[i]:
            selected[i] = True
            select_virus(i+1, cnt+1, v)
            selected[i] = False

#입력 조건
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
selected = [False] * 10 # 놓을 수 있는 바이러스의 개수는 최대 10

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

virus = [] # 바이러스의 위치 저장
no_wall = 0 # 빈 칸의 개수
for i in range(n):
    for j in range(n):
        # 해당 칸에 바이러스가 있다면 위치 저장
        if graph[i][j] == 2:
            virus.append((i, j))
        # 해당 칸이 빈 칸이라면 개수 증가
        elif graph[i][j] == 0:
            no_wall += 1

result = int(1e9)
queue = deque()
select_virus(0, 0, len(virus))

# 모든 빈 칸에 바이러스를 퍼뜨릴 수 없다면 -1 출력
if result == int(1e9):
    print(-1)
else:
    print(result)