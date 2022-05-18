def solution(rows, columns, queries):
    answer = []
    matrix = [[0 for _ in range(columns+1)] for _ in range(rows+1)]
    num = 1

    for row in range(1, rows+1):
        for column in range(1, columns+1):
            matrix[row][column] = num
            num += 1

    for x1, y1, x2, y2 in queries:
        temp = matrix[x1][y1]
        min_value = temp

        for k in range(x1, x2):
            cur = matrix[k+1][y1]
            matrix[k][y1] = cur
            min_value = min(min_value, cur)

        for k in range(y1, y2):
            cur = matrix[x2][k+1]
            matrix[x2][k] = cur
            min_value = min(min_value, cur)

        for k in range(x2, x1, -1):
            cur = matrix[k-1][y2]
            matrix[k][y2] = cur
            min_value = min(min_value, cur)

        for k in range(y2, y1, -1):
            cur = matrix[x1][k-1]
            matrix[x1][k] = cur
            min_value = min(min_value, cur)

        matrix[x1][y1+1] = temp
        answer.append(min_value)

    return answer

print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))
print(solution(3, 3, [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]))
print(solution(100, 97, [[1,1,100,97]]))

