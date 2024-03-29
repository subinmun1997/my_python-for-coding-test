n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
temp = [[0] * m for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 깊이 우선 탐색(dfs)을 이용해 각 바이러스가 사방으로 퍼지도록 하기
def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx, ny)

# 현재 맵에서 안전 영역의 크기 계산하는 메소드
def get_score():
    count = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                count += 1
    return count

result = 0
# 깊이 우선 탐색을 이용해 울타리를 설치하면서, 매번 안전 영역의 크기 계산
def dfs(count):
    global result
    # 울타리가 3개 설치된 경우
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = board[i][j]

        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)

        result = max(result, get_score())
        return

    # 빈 공간에 울타리 설치
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                board[i][j] = 1
                count += 1
                dfs(count)
                board[i][j] = 0
                count -= 1

dfs(0)
print(result)
