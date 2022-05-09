def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        if check(i) == "even":
            answer += i
        else:
            answer -= i

    return answer


def check(num):
    temp = 0
    for i in range(1, num+1):
        if num%i == 0:
            temp += 1
    return "even" if temp%2 == 0 else "odd"

print(solution(13, 17))
print(solution(24, 27))