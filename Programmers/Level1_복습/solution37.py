def solution(n, arr1, arr2):
    arr1 = binary(n, arr1)
    arr2 = binary(n, arr2)
    answer = []
    for i in range(n):
        temp = ''
        for j in range(n):
            if arr1[i][j] == '1' or arr2[i][j] == '1':
                temp += '#'
            elif arr1[i][j] == '0' and arr2[i][j] == '0':
                temp += ' '
        answer.append(temp)
    return answer

def binary(n, arr):
    for i in range(len(arr)):
        temp = ''
        while arr[i]:
            temp += str(arr[i]%2)
            arr[i] //= 2
        arr[i] = '0' * (n-len(temp)) + temp[::-1]
    return arr

print(solution(5, [9,20,28,18,11], [30,1,21,17,28]))
print(solution(6, [46,33,33,22,31,50], [27,56,19,14,14,10]))