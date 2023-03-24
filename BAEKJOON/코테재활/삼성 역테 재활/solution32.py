from copy import deepcopy

def watch(x, y, direction, temp):
    # 방향을 하나씩 확인하며 감시할 수 있는지 체크하기
    for d in direction:
        nx, ny = x, y
        while True:
            nx += dx[d]
            ny += dy[d]

            # 범위를 벗어나거나 or 벽이라면 끝내기
            if nx < 0 or nx >= n or ny < 0 or ny >= m or temp[nx][ny] == 6:
                break
            # 범위 내이고 빈 칸이라면 감시 할 수 있는 영역으로 표시
            if temp[nx][ny] == 0:
                temp[nx][ny] = '#'

def dfs(depth, graph):
    global result
    # 감시하는 영역을 반복 체크하기 위한 deepcopy
    temp = deepcopy(graph)

    # cctv의 개수만큼 감시 영역을 체크 했다면 사각지대 최소값 구하고 리턴
    if depth == len(cctv):
        cnt = 0
        for t in temp:
            cnt += t.count(0)

        result = min(result, cnt)
        return

    # cctv 저장 순서대로 (행, 열, 종류) 꺼내기
    x, y, c = cctv[depth]
    # 해당 cctv의 방향들을 차례대로 살펴보기
    for d in direction[c]:
        watch(x, y, d, temp)
        # 현 상태에서 또 다른 cctv 방향 체크하기 위해 재귀 호출
        dfs(depth+1, temp)
        # 새로 탐색을 시작하기 위함
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

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 사무실 내 cctv 위치와 종류 저장
cctv = []
for i in range(n):
    for j in range(m):
        if graph[i][j] != 0 and graph[i][j] != 6:
            cctv.append((i, j, graph[i][j]))

result = int(1e9)
dfs(0, graph)
print(result)