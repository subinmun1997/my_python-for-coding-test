def tenTobin(arr, n):
    binarr = []
    for i in arr:
        binarr.append(bin(i)[2:].zfill(n))
    return binarr

def solution(n, arr1, arr2):
    arr1 = tenTobin(arr1, n)
    arr2 = tenTobin(arr2, n)

    answer = []
    for i in range(n):
        temp = ''
        for j in range(n):
            if arr1[i][j] == '1' or arr2[i][j] == '1':
                temp += '#'
            else:
                temp += ' '
        answer.append(temp)

    return answer

print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
print(solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10]))