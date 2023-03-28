def solution(arr1, arr2):
    answer = [[0 for _ in range(len(arr2[0]))] for _ in range(len(arr1))]
    for x in range(len(arr1)):
        for y in range(len(arr2[0])):
            for z in range(len(arr1[0])):
                answer[x][y] += arr1[x][z] * arr2[z][y]

    return answer

print(solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]))
print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]))

'''
1 4     3 3
3 2     3 3
4 1
'''