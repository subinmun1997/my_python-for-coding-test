def solution(s):
    s = s.lower()
    return True if s.count('p') == s.count('y') else False

print(solution("pPoooyY"))
print(solution("Pyy"))
