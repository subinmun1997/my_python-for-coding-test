def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        if check_prime(i): # 약수의 개수가 짝수면 True 리턴
            answer += i
        else:
            answer -= i

    return answer

def check_prime(n):
    count = 0
    for i in range(1, n+1):
        if n%i == 0:
            count += 1

    return False if count%2 else True

print(solution(13, 17))
print(solution(24, 27))