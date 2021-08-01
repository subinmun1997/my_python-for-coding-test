def divisor(v):
    cnt = 0
    for i in range(1, v+1):
        if v%i == 0:
            cnt += 1
    return cnt

def solution(left, right):
    answer = 0

    for i in range(left, right+1):
        vl = divisor(i)

        if vl%2 == 0:
            answer += i
        else:
            answer -= i
    return answer

print(solution(13,17))
print(solution(24,27))
