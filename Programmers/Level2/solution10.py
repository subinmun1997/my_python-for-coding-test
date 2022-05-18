def solution(numbers, target):
    answer = 0
    prev = [0]
    for num in numbers:
        temp = []
        for i in prev:
            temp.append(i + num)
            temp.append(i - num)
        prev = temp
    for i in prev:
        if i == target:
            answer += 1

    return answer

print(solution([1, 1, 1, 1, 1], 3))
print(solution([4, 1, 2, 1], 4))