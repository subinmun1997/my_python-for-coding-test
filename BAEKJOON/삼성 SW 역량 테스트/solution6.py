from copy import deepcopy

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

def move(board, dir):
    if dir == 0: # 동쪽
        for i in range(n):
            top = n-1
            for j in range(n-2, -1, -1):
                if board[i][j]:
                    temp = board[i][j]
                    board[i][j] = 0
                    if board[i][top] == 0:
                        board[i][top] = temp
                    elif board[i][top] == temp:
                        board[i][top] = temp * 2
                        top -= 1
                    else:
                        top -= 1
                        board[i][top] = temp

    elif dir == 1: #서쪽
        for i in range(n):
            top = 0
            for j in range(1, n):
                if board[i][j]:
                    temp = board[i][j]
                    board[i][j] = 0
                    if board[i][top] == 0:
                        board[i][top] = temp
                    elif board[i][top] == temp:
                        board[i][top] = temp * 2
                        top += 1
                    else:
                        top += 1
                        board[i][top] = temp

    elif dir == 2: #남쪽
        for j in range(n):
            top = n-1
            for i in range(n-2, -1, -1):
                if board[i][j]:
                    temp = board[i][j]
                    board[i][j] = 0
                    if board[top][j] == 0:
                        board[top][j] = temp
                    elif board[top][j] == temp:
                        board[top][j] = temp * 2
                        top -= 1
                    else:
                        top -= 1
                        board[top][j] = temp

    else: #북쪽
        for j in range(n):
            top = 0
            for i in range(1, n):
                if board[i][j]:
                    temp = board[i][j]
                    board[i][j] = 0
                    if board[top][j] == 0:
                        board[top][j] = temp
                    elif board[top][j] == temp:
                        board[top][j] = temp * 2
                        top += 1
                    else:
                        top += 1
                        board[top][j] = temp

    return board


def dfs(board, cnt):
    global answer
    if cnt == 5:
        for i in range(n):
            for j in range(n):
                answer = max(answer, board[i][j])
        return

    for i in range(4):
        temp_board = move(deepcopy(board), i)
        dfs(temp_board, cnt + 1)


answer = 0
dfs(graph, 0)
print(answer)