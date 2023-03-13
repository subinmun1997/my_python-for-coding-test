'''
백트래킹을 이용해 모든 경우의 수에 대해 확인을 해야 하는 브루트포스 문제
상하좌우 x 5번 이동이므로 4^5(=1024)개의 경우만 고려하면 된다.
'''

from copy import deepcopy

def move(board, dir):
    if dir == 0: # 동쪽
        for i in range(n):
            top = n-1
            for j in range(n-2, -1, -1):
                if board[i][j]:
                    temp = board[i][j]
                    board[i][j] = 0
                    # top 위치의 수가 0일 때
                    if board[i][top] == 0:
                        board[i][top] = temp
                    # top 위치의 수와 현재 위치의 수가 같을 때
                    elif board[i][top] == temp:
                        board[i][top] *= 2
                        top -= 1
                    # top 위치의 수와 현재 위치의 수가 다를 때
                    else:
                        top -= 1
                        board[i][top] = temp
    elif dir == 1: # 서쪽
        for i in range(n):
            top = 0
            for j in range(1, n):
                if board[i][j]:
                    temp = board[i][j]
                    board[i][j] = 0

                    if board[i][top] == 0:
                        board[i][top] = temp
                    elif board[i][top] == temp:
                        board[i][top] *= 2
                        top += 1
                    else:
                        top += 1
                        board[i][top] = temp
    elif dir == 2: # 남쪽
        for j in range(n):
            top = n-1
            for i in range(n-2, -1, -1):
                if board[i][j]:
                    temp = board[i][j]
                    board[i][j] = 0

                    if board[top][j] == 0:
                        board[top][j] = temp
                    elif board[top][j] == temp:
                        board[top][j] *= 2
                        top -= 1
                    else:
                        top -= 1
                        board[top][j] = temp
    elif dir == 3: # 북쪽
        for j in range(n):
            top = 0
            for i in range(1, n):
                if board[i][j]:
                    temp = board[i][j]
                    board[i][j] = 0

                    if board[top][j] == 0:
                        board[top][j] = temp
                    elif board[top][j] == temp:
                        board[top][j] *= 2
                        top += 1
                    else:
                        top += 1
                        board[top][j] = temp

    return board

answer = 0
def dfs(board, cnt):
    global answer

    # 최대 5번 이동시켰다면 가장 큰 블록 출력
    if cnt == 5:
        for i in range(n):
            for j in range(n):
                answer = max(answer, board[i][j])
        return

    for i in range(4):
        # deepcopy를 해서 함수를 거친 board의 값이 다음 함수에 들어가지 못하도록 해주어야 한다
        temp_board = move(deepcopy(board), i)
        dfs(temp_board, cnt + 1)

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dfs(board, 0)
print(answer)