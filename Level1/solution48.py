def solution(x):
    answer = 0
    res = str(x)
    for i in range(len(res)):
        answer += int(res[i])
    if x%answer == 0:
        return True
    return False

print(solution(10))
print(solution(11))
print(solution(12))
print(solution(13))

# 한 줄 코드

# def solution(x):
#   return x% sum([int(c) for c in str(x)]) == 0