def solution(board, moves):
    result = 0
    stack = []

    for move in moves:
        for bor in board:
            if bor[move-1] != 0:
                temp = bor[move-1]
                bor[move-1] = 0
                if stack and temp == stack[-1]:
                    stack.pop()
                    result += 2
                    break
                else:
                    stack.append(temp)
                    break
    return result

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))