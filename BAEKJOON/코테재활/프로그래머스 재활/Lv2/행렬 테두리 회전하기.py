def solution(rows, columns, queries):
    answer = []
    arr = [[0 for _ in range(columns+1)] for _ in range(rows+1)]

    num = 1
    for i in range(1, rows+1):
        for j in range(1, columns+1):
            arr[i][j] = num
            num += 1

    for x1,y1,x2,y2 in queries:
        temp = arr[x1][y1]
        min_value = temp

        for k in range(x1, x2):
            cur = arr[k+1][y1]
            arr[k][y1] = cur
            min_value = min(min_value, cur)

        for k in range(y1, y2):
            cur = arr[x2][k+1]
            arr[x2][k] = cur
            min_value = min(min_value, cur)

        for k in range(x2, x1, -1):
            cur = arr[k-1][y2]
            arr[k][y2] = cur
            min_value = min(min_value, cur)

        for k in range(y2, y1, -1):
            cur = arr[x1][k-1]
            arr[x1][k] = cur
            min_value = min(min_value, cur)

        arr[x1][y1+1] = temp
        answer.append(min_value)

    return answer

print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))
print(solution(3, 3, [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]))
print(solution(100, 97, [[1,1,100,97]]))