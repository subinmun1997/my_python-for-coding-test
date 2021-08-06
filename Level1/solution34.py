def solution(n):
    answer = ''
    for i in range(n):
        if i%2 == 0:
            answer += '수'
        else:
            answer += '박'

    return answer

print(solution(3))
print(solution(4))

# 다른 코드1
# def solution(n):
#   s = '수박' * n
#   return s[:n]



# 다른 코드2
# def solution(n):
#   return "수박"*(n//2) + "수"*(n%2)
#