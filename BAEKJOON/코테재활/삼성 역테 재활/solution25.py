"""

"""

"""
1. 인접한 네 개의 칸 중 나무가 있는 칸의 수만큼 나무가 성장합니다. 성장은 모든 나무에게 동시에 일어납니다.
-> 모든 격자판이 0으로 된 n*n 배열을 새로 만들고, 원래 격자판의 4방향 탐색을 통해 인접한 나무 칸을 세고 새로 만든 배열에 나무 칸의 개수만큼
더해준 다음 최종적으로 원래 격자판에 다 더해준다.

2. 기존에 있었던 나무들은 인접한 4개의 칸 중 벽, 다른 나무, 제초제 모두 없는 칸에 번식을 진행합니다.
이때 각 칸의 나무 그루 수에서 총 번식이 가능한 칸의 개수만큼 나누어진 그루 수만큼 번식이 되며, 나눌 때 생기는 나머지는 버립니다.
번식의 과정은 모든 나무에서 동시에 일어나게 됩니다.
-> 원래 격자판을 복사한 배열을 만든다. 그리고 원래 격자판 끼리 4방향 탐색으로 빈칸을 찾고 번식하는 과정은 복사한 배열에 해주고 마지막에 원래 격자판에 복사해준다.

3.각 칸 중 제초제를 뿌렸을 때 나무가 가장 많이 박멸되는 칸에 제초제를 뿌립니다. 제초제를 뿌릴 때 4개의 대각선 방향으로 k칸만큼 전파되게 됩니다.
단 전파되는 도중 벽이 있거나 나무가 아얘 없는 칸이 있는 경우, 그 칸 까지는 제초제가 뿌려지며 그 이후의 칸으로는 제초제가 전파되지 않습니다.
제초제가 뿌려진 칸에는 c년만큼 제초제가 남아있다가 c+1년째가 될 때 사라지게 됩니다.
제초제가 뿌려진 곳에 다시 제초제가 뿌려지는 경우에는 새로 뿌려진 해로부터 다시 c년동안 제초제가 유지됩니다.
-> ...
"""

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

    kill_tree[x][y] = c #기존 제초제가 뿌려져 있는 칸에 또 다시 뿌리게 되면 새로 년 수를 셈
    graph[x][y] = 0 # 제초제를 뿌린 위치는 나무 0

    for p in range(4):
        cur_x, cur_y = x, y
        for _ in range(k):
            nx = cur_x + d_dx[p]
            ny = cur_y + d_dy[p]

            if not (0 <= nx < n and 0 <= ny < n):
                break

            if graph[nx][ny] == -1: # 벽일때는 제초제를 안뿌려도 됨.
                break

            if graph[nx][ny] == 0: # 빈칸일때는 제초제를 뿌리고 더이상 뿌리지 않음.
                kill_tree[nx][ny] = c
                break

            if graph[nx][ny] >= 1:
                kill_tree[nx][ny] = c
                graph[nx][ny] = 0
                cur_x, cur_y = nx, ny


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