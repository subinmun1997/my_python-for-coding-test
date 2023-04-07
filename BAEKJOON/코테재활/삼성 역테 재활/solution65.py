from copy import deepcopy

def grow():
    new_graph = [[0] * n for _ in range(n)]

    for x in range(n):
        for y in range(n):
            if graph[x][y] >= 1:

                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]

                    if 0 <= nx < n and 0 <= ny < n:
                        if graph[nx][ny] >= 1:
                            new_graph[nx][ny] += 1

    for x in range(n):
        for y in range(n):
            graph[x][y] += new_graph[x][y]

def spread():
    new_graph = deepcopy(graph)

    for x in range(n):
        for y in range(n):
            if graph[x][y] >= 1:

                tree_amount = graph[x][y]
                cnt = 0
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]

                    if 0 <= nx < n and 0 <= ny < n:
                        if graph[nx][ny] == 0 and kill_tree[nx][ny] == 0:
                            cnt += 1

                if cnt != 0:
                    spread_amount = tree_amount // cnt

                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]

                        if 0 <= nx < n and 0 <= ny < n:
                            if graph[nx][ny] == 0 and kill_tree[nx][ny] == 0:
                                new_graph[nx][ny] += spread_amount

    return new_graph


d_dx = [1, 1, -1, -1]
d_dy = [1, -1, 1, -1]
def most_tree_kill(x, y):
    global pre_x, pre_y, kill_amount

    value = graph[x][y]

    for i in range(4):
        cur_x, cur_y = x, y
        for _ in range(k):
            nx = cur_x + d_dx[i]
            ny = cur_y + d_dy[i]

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

def kill_tree_time():
    for i in range(n):
        for j in range(n):
            if kill_tree[i][j] > 0:
                kill_tree[i][j] -= 1


def tree_kill(x, y):
    kill_tree[x][y] = c
    graph[x][y] = 0

    for i in range(4):
        cur_x, cur_y = x, y
        for _ in range(k):
            nx = cur_x + d_dx[i]
            ny = cur_y + d_dy[i]

            if not (0 <= nx < n and 0 <= ny < n):
                break

            if graph[nx][ny] <= 0:
                kill_tree[nx][ny] = c
                break

            if graph[nx][ny] >= 1:
                kill_tree[nx][ny] = c
                graph[nx][ny] = 0
                cur_x, cur_y = nx, ny

# n=격자의 크기, m=박멸이 진행되는 년 수, k=제초제의 확산 범위, c=제초제가 남아있는 년 수
n, m, k, c = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
# 제초제가 남아있는 년 수 저장 배열
kill_tree = [[0] * n for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 출력 조건, m년 동안 박멸한 나무의 총 그루 수
answer = 0
for _ in range(m):
    # 1. 나무의 성장
    grow()

    # 2. 나무의 번식
    graph = spread()

    # 3. 제초제 뿌릴 구역 정하기
    pre_x, pre_y = 0, 0
    kill_amount = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] >= 1:
                most_tree_kill(i, j)

    # 4. 제초제 시간을 줄여준다
    kill_tree_time()

    # 5. 제초제를 살포한다
    tree_kill(pre_x, pre_y)

    answer += kill_amount

print(answer)