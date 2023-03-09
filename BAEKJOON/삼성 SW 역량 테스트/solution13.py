from collections import deque

def move(i, j, dx, dy):
    c = 0
    # 다음으로 이동할 칸이 벽이 아니면서 해당 위치가 구멍이 아닐때 까지
    while board[i+dx][j+dy] != '#' and board[i][j] != 'O':
        i += dx
        j += dy
        c += 1

    return i, j, c

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def bfs():
    while queue:
        ri, rj, bi, bj, d = queue.popleft()
        if d > 10: # 10번 이하로 움직여서 빨간 구슬을 구멍을 통해 빼낼 수 없으면 -1 출력
            break
        for i in range(4):
            # 상하좌우로 돌면서 최대한 굴리기
            nri, nrj, rc = move(ri, rj, dx[i], dy[i])
            nbi, nbj, bc = move(bi, bj, dx[i], dy[i])

            if board[nbi][nbj] != 'O': # 파란 구슬은 빼지 못하는 상황에서
                if board[nri][nrj] == 'O': # 빨간 구슬을 뺄 수 있다면 출력하고 끝내기
                    print(d)
                    return
                if nri == nbi and nrj == nbj: # 두 개의 공이 동일한 위치에 있다면 더 많이 구른 구슬을 이전으로 보내기
                    if rc < bc:
                        nbi -= dx[i]
                        nbj -= dy[i]
                    else:
                        nri -= dx[i]
                        nrj -= dy[i]
                if not visited[nri][nrj][nbi][nbj]: # 해당 위치가 방문하지 않았던 위치라면 방문 체크하고 큐에 넣기
                    visited[nri][nrj][nbi][nbj] = True
                    queue.append([nri, nrj, nbi, nbj, d+1])

    print(-1)

n, m = map(int, input().split())

board = []
for i in range(n): # n번동안 한줄씩 입력받으며 'R'의 위치와 'B'의 위치 저장해놓기
    a = list(input())
    board.append(a)
    for j in range(m):
        if a[j] == 'R':
            ri, rj = i, j
        if a[j] == 'B':
            bi, bj = i, j

queue = deque()
queue.append([ri, rj, bi, bj, 1])
visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
visited[ri][rj][bi][bj] = True
bfs()