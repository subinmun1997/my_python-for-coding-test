def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        if check(i):
            answer += i
        else:
            answer -= i
    return answer

def check(num):
    count = 0
    for i in range(1, num+1):
        if num%i == 0:
            count += 1
    return True if count%2 == 0 else False # 짝수면 true, 홀수면 false

print(solution(13, 17))
print(solution(24, 27))