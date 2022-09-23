n = int(input())

board = [list(map(int, input().split())) for _ in range(n)]

result_minus = 0
result_zero = 0
result_plus = 0

def dfs(x,y,n):
    global result_minus, result_zero, result_plus

    num_check = board[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if board[i][j] != num_check:
                for k in range(3):
                    for l in range(3):
                        dfs(x+k*n//3, y+l*n//3, n//3)
                return

    if num_check == -1:
        result_minus += 1
    elif num_check == 0:
        result_zero += 1
    else:
        result_plus += 1

dfs(0,0,n)
print(f"{result_minus}\n{result_zero}\n{result_plus}")