def solution(k, score):
    stack = []
    answer = []

    for i in score:
        stack.append(i)
        if len(stack) > k:
            stack.remove(min(stack))
        answer.append(min(stack))

    return answer

print(solution(3, [10, 100, 20, 150, 1, 100, 200]))
print(solution(4, [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]))