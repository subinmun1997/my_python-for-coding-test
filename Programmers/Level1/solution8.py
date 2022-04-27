def solution(s):
    s = s.lower()
    return True if s.count('p') == s.count('y') else False

print(solution("pPoooyY"))
print(solution("Pyy"))

"""
다른 풀이
def solution(s):
    return s.lower().count('p') == s.lower().count('y')
"""