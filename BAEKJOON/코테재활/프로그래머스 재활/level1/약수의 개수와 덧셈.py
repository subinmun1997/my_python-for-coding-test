def check(num):
    cnt = 0
    for i in range(1, num+1):
        if num % i == 0:
            cnt += 1

    return True if cnt % 2 == 0 else False
def solution(left, right):
    answer = 0
    for num in range(left, right+1):
        if check(num):
            answer += num
        else:
            answer -= num

    return answer

print(solution(13, 17))
print(solution(24, 27))