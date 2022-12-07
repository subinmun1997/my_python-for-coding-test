def solution(n, arr1, arr2):
    board1, board2 = [], []
    for i in range(n):
        c1 = bin(arr1[i])[2:]
        while len(c1) != n:
            c1 = '0' + c1
        board1.append(c1)
        c2 = bin(arr2[i])[2:]
        while len(c2) != n:
            c2 = '0' + c2
        board2.append(c2)

    result = []
    for i in range(n):
        temp = ''
        for j in range(n):
            if board1[i][j] == '1' or board2[i][j] == '1':
                temp += '#'
            else:
                temp += ' '
        result.append(temp)

    return result

print(solution(5, [9,20,28,18,11], [30,1,21,17,28]))
print(solution(6, [46,33,33,22,31,50], [27,56,19,14,14,10]))