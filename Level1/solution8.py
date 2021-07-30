def solution(a, b):
    answer = 0
    for i in range(len(a)):
        answer += a[i]*b[i]
    return answer

# 한 줄 코드
# def solution(a, b):
#   return sum(x*y for x, y in zip(a,b))