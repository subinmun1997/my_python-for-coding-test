def solution(n, arr1, arr2):
    first = binary(arr1, n)
    second = binary(arr2, n)
    total = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if first[i][j] == '1' or second[i][j] == '1':
                total[i].append('#')
            else:
                total[i].append(' ')
    answer = []
    for i in total:
       answer.append(''.join(i))
    return answer

def binary(arr, n):
    result = []
    for i in arr:
        temp = ''
        while i:
            temp += str(i%2)
            i //= 2
        if len(temp) < n:
            temp += (n - len(temp)) * '0'
        result.append(temp[::-1])
    return result

print(solution(5, [9,20,28,18,11], [30,1,21,17,28]))
print(solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10]))