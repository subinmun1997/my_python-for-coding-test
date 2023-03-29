from copy import deepcopy

def watch(x, y, direction, temp):
    # 방향 하나씩 확인하기
    for d in direction:
        nx, ny = x, y
        while True:
            nx += dx[d]
            ny += dy[d]
            # 범위 내이고 벽이 아니라면 표시하기
            if nx < 0 or nx >= n or ny < 0 or ny >= m or temp[nx][ny] == 6:
                break
            if temp[nx][ny] == 0:
                temp[nx][ny] = '#'

def dfs(depth, graph):
    global result
    # 원본 그래프 변경하면 안되니, deepcopy
    temp = deepcopy(graph)

    # CCTV 종류만큼 다 확인했으면 사각지대 최솟값 구하기
    if depth == len(cctv):
        cnt = 0
        for t in temp:
            cnt += t.count(0)
        result = min(result, cnt)
        return

    x, y, c = cctv[depth]
    # 한 방향씩 확인하며 체크
    for d in direction[c]:
        watch(x, y, d, temp)
        # 현 상태에서 다른 cctv 방향 체크하기 위한 재귀호출
        dfs(depth+1, temp)
        # 새로 탐색하기 위한 deepcopy 다시
        temp = deepcopy(graph)

# 입력 조건
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# CCTV별 감시할 수 있는 방향
direction = {
    1: [[0], [1], [2], [3]],
    2: [[0, 2], [1, 3]],
    3: [[0, 1], [1, 2], [2, 3], [3, 0]],
    4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    5: [[0, 1, 2, 3]]
}

# 상하좌우 CCTV 회전
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# cctv의 위치와 종류 저장
cctv = []
for i in range(n):
    for j in range(m):
        # 빈 칸이 아니고 벽도 아니라면 cctv이다
        if graph[i][j] != 0 and graph[i][j] != 6:
            # (위치, 종류) 저장
            cctv.append((i, j, graph[i][j]))

result = int(1e9)
dfs(0, graph)

print(result)