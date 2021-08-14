def solution(s):
    answer = list(map(int, s.split(' ')))
    return str(min(answer)) + ' ' + str(max(answer))

print(solution("1 2 3 4"))
print(solution("-1 -2 -3 -4"))
print(solution("-1 -1"))