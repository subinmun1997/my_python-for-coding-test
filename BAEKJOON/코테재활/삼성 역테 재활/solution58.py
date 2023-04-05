from copy import deepcopy

def grow(): # 1단계 -> 나무의 성장
    new_graph = [[0] * n for _ in range(n)]

    for x in range(n):
        for y in range(n):
            if graph[x][y] >= 1:

                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]

                    if 0 <= nx < n and 0 <= ny < n:
                        if graph[nx][ny] >= 1:
                            new_graph[x][y] += 1

    for x in range(n):
        for y in range(n):
            graph[x][y] += new_graph[x][y]

def spread(): # 2단계 -> 나무의 확산
    new_graph = deepcopy(graph)

    for i in range(n):
        for j in range(n):
            if graph[i][j] >= 1:

                tree_amount = graph[i][j] # 타겟이 되는 위치의 나무 그루 수
                cnt = 0 # 벽X, 다른 나무X, 제초제X 칸의 개수
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]

                    if 0 <= nx < n and 0 <= ny < n:
                        # 빈칸이고 남아있는 제초제가 없는 칸이라면
                        if graph[nx][ny] == 0 and kill_tree[nx][ny] == 0:
                            cnt += 1

                if cnt != 0:
                    spread_amount = tree_amount // cnt

                    for k in range(4):
                        nx = i + dx[k]
                        ny = j + dy[k]

                        if 0 <= nx < n and 0 <= ny < n:
                            # 다른 나무가 없고, 제초제가 없다면 확산
                            if graph[nx][ny] == 0 and kill_tree[nx][ny] == 0:
                                new_graph[nx][ny] += spread_amount

    return new_graph

# 대각선 좌표
d_dx = [-1, -1, 1, 1]
d_dy = [-1, 1, -1, 1]
def most_tree_kill(x, y): # 3단계 -> 가장 많은 나무를 죽일 수 있는 위치를 찾는 함수
    global pre_x, pre_y, kill_amount

    value = graph[x][y] # 제초제로 죽일 수 있는 나무의 양

    for p in range(4):
        cur_x, cur_y = x, y
        for _ in range(k):
            nx = cur_x + d_dx[p]
            ny = cur_y + d_dy[p]

            if not (0 <= nx < n and 0 <= ny < n):
                break

            if graph[nx][ny] <= 0:
                break

            if graph[nx][ny] >= 1:
                value += graph[nx][ny]
                cur_x, cur_y = nx, ny


    if kill_amount < value:
        pre_x, pre_y = x, y
        kill_amount = value

def tree_kill(x, y): # 4단계 -> 나무를 죽이는 제초제를 뿌리는 함수.

    kill_tree[x][y] = c
    graph[x][y] = 0

    for p in range(4):
        cur_x, cur_y = x, y
        for _ in range(k):
            mx = cur_x + d_dx[p]
            my = cur_y + d_dy[p]

            if not (0 <= mx < n and 0 <= my < n):
                break

            if graph[mx][my] == -1: # 벽일때는 제초제를 안뿌려도 됨.
                break

            if graph[mx][my] == 0: # 빈칸일때는 제초제를 뿌리고 더이상 뿌리지 않음.
                kill_tree[mx][my] = c
                break

            if graph[mx][my] >= 1:
                kill_tree[mx][my] = c
                graph[mx][my] = 0
                cur_x, cur_y = mx, my

def kill_tree_time():

    for i in range(n):
        for j in range(n):
            if kill_tree[i][j] > 0:
                kill_tree[i][j] -= 1

n, m, k, c = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
kill_tree = [[0] * n for _ in range(n)] # 제초제 남아있는 칸 작성 배열
answer = 0

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# m년 간 박멸한 나무의 그루 수 구하기
for _ in range(m):

    # 1단계: 나무 성장
    grow()

    # 2단계: 상하좌우 나무 번식
    graph = spread()

    # 3단계: 나무 제일 많이 박멸시킬 수 있는 칸 찾기
    pre_x, pre_y = 0, 0
    kill_amount = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] >= 1:
                most_tree_kill(i, j)

    # 4. 제초제 시간을 줄여준다.
    kill_tree_time()

    # 5. 제초제를 살포한다.
    tree_kill(pre_x, pre_y)

    answer += kill_amount

print(answer)