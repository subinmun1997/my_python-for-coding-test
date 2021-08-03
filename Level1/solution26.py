def solution(arr, divisor):
    answer = []
    for i in arr:
        if i%divisor == 0:
            answer.append(i)

    if answer:
        return sorted(answer)
    else:
        answer.append(-1)
        return answer

# 한 줄 코드
# def solution(arr, divisor):
#  return sorted([n for n in arr if n%d == 0]) or [-1]