def solution(n):
    res = str(n)
    answer = []

    for i in range(len(res)):
        answer.append(int(res[i]))
    answer.reverse()

    return answer

print(solution(12345))

# 한 줄 코드

# def solution(n):
#   return [int(i) for i in str(n)][::-1]
#