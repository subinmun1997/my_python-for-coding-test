'''
문제에서 최소 몇 번 만에 탐색할 수 있는가를 묻고 있기 때문에 BFS로 풀어야 한다.
'''
from collections import deque

# 빨간 구슬과 파란 구슬 모두 위, 아래, 왼, 오른쪽으로 이동하는데
# 벽(#)이거나 구멍(O) 전까지 직진
def move(i, j, dx, dy):
    c = 0
    while board[i+dx][j+dy] != '#' and board[i][j] != 'O':
        c += 1
        i += dx
        j += dy

    return i, j, c

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def bfs():
    while queue:
        ri, rj, bi, bj, d = queue.popleft()
        if d > 10:
            break
        for i in range(4):
            nri, nrj, rc = move(ri, rj, dx[i], dy[i])
            nbi, nbj, bc = move(bi, bj, dx[i], dy[i])
            # 파란 구슬이 구멍을 만나면 실패이므로 파란 구슬이 구멍을 만나지 않을때 체크
            if board[nbi][nbj] != 'O':
                # 빨간 구슬이 구멍을 만나면 횟수 출력하고 끝내기
                if board[nri][nrj] == 'O':
                    print(d)
                    return
                # 만약에 빨간 구슬과 파란 구슬이 겹쳐졌다는 것은 하나는 막혀서 멈춰있는데
                # 다른 하나가 다가온 것이므로 이럴경우 더 늦게 도착한 애를 하나 뒤로 움직여줘야 한다.
                # 이것을 위해 구슬의 이동거리를 세어줘야함
                if nri == nbi and nrj == nbj:
                    if bc < rc:
                        nri -= dx[i]
                        nrj -= dy[i]
                    else:
                        nbi -= dx[i]
                        nbj -= dy[i]
                if not visited[nri][nrj][nbi][nbj]:
                    visited[nri][nrj][nbi][nbj] = True
                    queue.append([nri, nrj, nbi, nbj, d+1])

    print(-1)

n, m = map(int, input().split()) # 보드의 세로, 가로 크기

board = []
for i in range(n):
    a = list(input())
    board.append(a)
    for j in range(m): # 빨간 구슬, 파란 구슬의 위치 저장
        if a[j] == 'R':
            ri, rj = i, j
        if a[j] == 'B':
            bi, bj = i, j

# 방문처리 할 배열을 4차원으로 정의한다. (빨간 구슬과 파란 구슬을 함께 체크하기 위함)
visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
queue = deque()
# 초기의 빨간 구슬과 파란 구슬의 위치를 큐에 삽입
queue.append([ri, rj, bi, bj, 1])
visited[ri][rj][bi][bj] = True
bfs()
