def solution(board, moves):
    stack = []
    count = 0
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1]:
                if stack and stack[-1] == board[j][i-1]:
                    count += 2
                    stack.pop()
                    board[j][i-1] = 0
                    break
                else:
                    stack.append(board[j][i-1])
                    board[j][i-1] = 0
                    break

    return count

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))