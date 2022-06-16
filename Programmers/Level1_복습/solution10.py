def solution(s):
    # len(s) 값이 [4,6]리스트에 포함되어 있나
    return len(s) in [4, 6] and s.isdigit()

print(solution("a234"))
print(solution("1234"))
