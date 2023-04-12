from collections import deque

# 보드의 크기
n = int(input())
board = [[0 for _ in range(n+1)] for _ in range(n+1)]

# 사과의 개수
k = int(input())
for _ in range(k):
    x, y = map(int, input().split())
    # 사과가 있으면 1로 표시
    board[x][y] = 1

# 뱀의 방향 변환 횟수
l = int(input())
move = []
for _ in range(l):
    x, c = input().split()
    move.append((int(x), c))

dx = [0, 1, 0, -1] # 우 하 좌 상
dy = [1, 0, -1, 0]

def turn(direction, c):
    if c == 'L':
        direction = (direction - 1) % 4
    elif c == 'D':
        direction = (direction + 1) % 4

    return direction

queue = deque()
def simulate():
    # 뱀의 처음 위치
    x, y = 1, 1
    queue.append((x, y))
    # 뱀이 있는 위치는 2로 표시
    board[x][y] = 2
    index = 0
    # 게임이 시작하고 몇 초가 흘렀는지
    time = 0
    # 뱀은 처음에는 오른쪽을 향한다
    direction = 0

    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]

        # 이동하려는 위치가 범위 내이고, 뱀 자기자신의 몸이 있는 칸이 아니라면
        if 1 <= nx <= n and 1 <= ny <= n and board[nx][ny] != 2:
            # 해당 위치에 사과가 있으면
            if board[nx][ny] == 1:
                # 사과를 없애고 뱀 머리 이동시켜주기
                board[nx][ny] = 2
                queue.append((nx, ny))
            # 사과는 없고 빈 칸이라면
            elif board[nx][ny] == 0:
                board[nx][ny] = 2
                queue.append((nx, ny))
                # 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다
                px, py = queue.popleft()
                board[px][py] = 0
        # 범위를 벗어났거나(벽) 자기자신의 몸과 부딪혔다면 시간 하나 늘려주고 종료하기
        else:
            time += 1
            break

        x, y = nx, ny
        time += 1
        # 방향 전환 시간이 되었으면
        if index < l and time == move[index][0]:
            direction = turn(direction, move[index][1])
            index += 1

    return time

print(simulate())