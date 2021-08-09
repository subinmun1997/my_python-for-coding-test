def solution(n):
    answer = 0
    a = str(n)

    for i in range(len(a)):
        answer += int(a[i])

    return answer

print(solution(123))
print(solution(987))

# 재귀를 이용한 코드

# def solution(n):
#   if n<10:
#       return n
#   return (n%10) + solution(n//10)