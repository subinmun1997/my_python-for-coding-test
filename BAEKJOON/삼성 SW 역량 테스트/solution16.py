from collections import deque

n = int(input()) # 보드의 크기
k = int(input()) # 사과의 개수

# 보드의 가장자리는 벽이므로 길이 n+1, 높이 n+1로 생성
board = [[0 for _ in range(n+1)] for _ in range(n+1)]
# 사과의 위치 저장 (사과=1)
for _ in range(k):
    x, y = map(int, input().split())
    board[x][y] = 1

l = int(input()) # 뱀의 뱡향 변환 횟수
move = [] # 뱀의 뱡향 변환 정보
for _ in range(l):
    x, c = input().split()
    move.append((int(x), c))

dx = [0, 1, 0, -1] # 동 남 서 북
dy = [1, 0, -1, 0]
# 방향 전환 함수
def turn(direction, c):
    if c == 'L': # 왼쪽으로 90도 회전
        direction = (direction - 1) % 4
    else: # 오른쪽으로 90도 회전
        direction = (direction + 1) % 4

    return direction

queue = deque()
def simulate():
    x, y = 1, 1 # 뱀의 처음 위치는 (1,1)
    queue.append((x, y))
    board[x][y] = 2 # 뱀 위치 저장

    direction = 0 # 뱀은 처음에 오른쪽을 향한다
    time = 0 # 몇 초가 지난 후 게임이 끝나는지
    index = 0 # 방향 전환 횟수 카운트
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]

        # 범위 내의 값이고 해당 위치에 뱀 자기자신의 몸이 없다면
        if 1 <= nx <= n and 1 <= ny <= n and board[nx][ny] != 2:
            if board[nx][ny] == 1: # 사과가 있으면 큐에 저장(길이 1 증가됨)
                board[nx][ny] = 2
                queue.append((nx, ny))
            elif board[nx][ny] == 0: # 사과가 없으면 뱀의 위치만 옮겨주고 길이는 동일
                board[nx][ny] = 2
                queue.append((nx, ny))
                px, py = queue.popleft()
                board[px][py] = 0
        else: # 범위를 벗어나거나 뱀 자기자신의 몸과 부딪혔다면 시간 1 늘려주고 끝내기
            time += 1
            break

        x, y = nx, ny
        time += 1
        # index가 방향 변환 횟수보다 작고 이동할 시간이라면
        if index < l and time == move[index][0]:
            direction = turn(direction, move[index][1])
            index += 1

    return time

print(simulate())