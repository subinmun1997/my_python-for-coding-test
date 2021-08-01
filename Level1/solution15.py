def solution(n):
    result = []

    while n:
        result.append(n%3)
        n //= 3

    answer = 0
    for r in result:
        answer = answer * 3 + r

    return answer

print(solution(45))
print(solution(125))

# 다른 코드
# def solution(n):
#   tmp = ''
#   while n:
#       tmp += str(n%3)
#       n //= 3
#   answer = int(tmp,3) # int(문자열, 진수)는 숫자 형태의 문자열을 해당 진수 값으로 인식하고 이 값을 10진수 숫자로 변환하는 역할
#   return answer