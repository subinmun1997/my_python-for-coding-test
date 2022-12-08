def solution(array, commands):
    answer = []
    for command in commands:
        x, y, z = command
        answer.append(sorted(array[x-1:y])[z-1])
    return answer

print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))