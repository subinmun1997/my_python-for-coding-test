def solution(a, b):
    a, b = map(int, input().strip().split(' '))

    answer = ('*' * a + '\n') * b

    return answer

print(solution(5,3))
print(solution(4,2))