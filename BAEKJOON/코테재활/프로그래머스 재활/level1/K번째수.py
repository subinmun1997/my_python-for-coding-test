def solution(array, commands):
    answer = []
    for x, y, target in commands:
        answer.append(sorted(array[x-1:y])[target-1])
    return answer

print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))