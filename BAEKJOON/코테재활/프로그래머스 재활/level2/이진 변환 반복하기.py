def solution(s):
    count = 0 #이진 변환의 횟수
    zero = 0 # 제거된 0의 개수

    while s != "1":
        count += 1
        zero += s.count('0')
        s = s.replace('0', '')
        s = str(bin(len(s))[2:])

    return [count, zero]

print(solution("110010101001"))
print(solution("01110"))
print(solution("1111111"))