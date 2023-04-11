from collections import deque

def move(i, j, dx, dy):
    c = 0
    # 현재 위치가 구멍이 아니고, 다음 위치가 벽이 아니라면 굴리기
    while graph[i+dx][j+dy] != '#' and graph[i][j] != 'O':
        c += 1
        i += dx
        j += dy

    return i, j, c

def bfs():
    while queue:
        ri, rj, bi, bj, d = queue.popleft()
        # 10번 이하로 움직여서 빨간 구슬을 구멍을 통해 빼낼 수 없으면 -1 출력
        if d > 10:
            break
        for i in range(4):
            # move 함수: 상하좌우로 갈 수 있을 때까지 굴리기
            nri, nrj, rc = move(ri, rj, dx[i], dy[i])
            nbi, nbj, bc = move(bi, bj, dx[i], dy[i])
            # 파란 구슬은 구멍에 빠지지 않은 상황을 가정
            if graph[nbi][nbj] != 'O':
                # 빨간 구슬이 구멍에 빠졌다면 걸린 횟수 출력하고 종료
                if graph[nri][nrj] == 'O':
                    print(d)
                    return
                # 빨간 구슬과 파란 구슬이 겹쳐졌다면
                if nri == nbi and nrj == nbj:
                    # 빨간 구슬의 이동 횟수가 더 많다면 한 칸 뒤로 이동
                    if bc < rc:
                        nri -= dx[i]
                        nrj -= dy[i]
                    # 파란 구슬의 이동 횟수가 더 많다면 한 칸 뒤로 이동
                    else:
                        nbi -= dx[i]
                        nbj -= dy[i]

                # 구슬 위치가 방문한 적 없는 위치라면 방문처리 해주고
                # 큐에 삽입
                if not visited[nri][nrj][nbi][nbj]:
                    visited[nri][nrj][nbi][nbj] = True
                    queue.append([nri, nrj, nbi, nbj, d+1])
    print(-1)

# n=세로, m=가로
n, m = map(int, input().split())
# n * m 보드
graph = []
for i in range(n):
    # 한 줄씩 입력 받기
    a = list(input())
    graph.append(a)
    for j in range(m):
        # 빨간 구슬이 들어있다면 위치 기록해놓기
        if a[j] == 'R':
            ri, rj = i, j
        # 파란 구슬이 들어있다면 위치 기록해놓기
        elif a[j] == 'B':
            bi, bj = i, j

# 구슬의 이동 방향 (상 우 하 좌)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
# 구슬의 위치를 저장하기 위한 4차원 배열
visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
# 최초 구슬 위치 True로 저장
visited[ri][rj][bi][bj] = True

queue = deque()
queue.append([ri, rj, bi, bj, 1])
bfs()