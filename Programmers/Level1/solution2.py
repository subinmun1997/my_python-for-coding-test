def solution(x):
    answer = 0
    str_x = str(x)
    for i in str_x:
        answer += int(i)
    if x % answer == 0:
        return True
    else:
        return False

print(solution(10))
print(solution(12))
print(solution(11))
print(solution(13))