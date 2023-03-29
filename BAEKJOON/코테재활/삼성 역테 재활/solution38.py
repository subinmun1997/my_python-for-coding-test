from copy import deepcopy

def watch(x, y, direction, temp):
    # 한 개의 방향씩 살펴보며 감시할 수 있는 곳 체크하기
    for d in direction:
        nx, ny = x, y
        while True:
            nx += dx[d]
            ny += dy[d]

            # 범위 밖이거나 벽이면 감시 멈춤
            if nx < 0 or nx >= n or ny < 0 or ny >= m or temp[nx][ny] == 6:
                break
            # 빈 칸이면 감시 영역으로 추가
            if temp[nx][ny] == 0:
                temp[nx][ny] = '#'

def dfs(depth, graph):
    global result
    # 원래 그래프 변경되면 안되기 때문에 복사해서 사용
    temp = deepcopy(graph)

    # 사무실 내의 모든 cctv를 확인했다면 사각지대 최솟값 찾기
    if depth == len(cctv):
        cnt = 0
        for t in temp:
            cnt += t.count(0)
        result = min(result, cnt)
        return

    x, y, d = cctv[depth]
    # 해당 cctv 종류로 살펴볼 수 있는 방향 하나씩 체크
    for c in direction[d]:
        watch(x, y, c, temp)
        # 현재 상태에서 또 다른 cctv 감시까지 진행
        dfs(depth+1, temp)
        # 새로운 탐색을 위한 재복사
        temp = deepcopy(graph)

# 입력 조건
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# 각 cctv별 회전 가능한 방향
direction = {
    1: [[0], [1], [2], [3]],
    2: [[0, 2], [1, 3]],
    3: [[0, 1], [1, 2], [2, 3], [3, 0]],
    4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    5: [[0, 1, 2, 3]]
}

# cctv는 90도 방향으로 회전 가능하다 (상, 하, 좌, 우 선언)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

cctv = []
for i in range(n):
    for j in range(m):
        # 빈 칸이 아니고, 벽도 아니라면 cctv
        if graph[i][j] != 0 and graph[i][j] != 6:
            # cctv의 위치와 종류 저장
            cctv.append((i, j, graph[i][j]))

# 출력 조건: 사각 지대의 최소 크기
result = int(1e9)
dfs(0, graph)

print(result)