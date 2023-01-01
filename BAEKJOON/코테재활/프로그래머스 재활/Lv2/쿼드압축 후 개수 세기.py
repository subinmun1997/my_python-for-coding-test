def solution(arr):
    answer = [0, 0]
    arrLen = len(arr)

    def quard(x, y, n):
        first = arr[x][y]

        for i in range(x, x+n):
            for j in range(y, y+n):
                if arr[i][j] != first:
                    n //= 2
                    quard(x, y, n)
                    quard(x, y+n, n)
                    quard(x+n, y, n)
                    quard(x+n, y+n, n)
                    return

        answer[first] += 1

    quard(0, 0, arrLen)
    return answer

print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))
print(solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]))