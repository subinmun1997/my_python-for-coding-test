def check(arr):
    stack = []
    for i in arr:
        if i in ['[', '{', '(']:
            stack.append(i)
        elif i == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                return False
        elif i == '}':
            if stack and stack[-1] == '{':
                stack.pop()
            else:
                return False
        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                return False

    return False if stack else True

def solution(s):
    result = 0
    for i in range(len(s)):
        move = s[i:] + s[:i]
        if check(move):
            result += 1

    return result

print(solution("[](){}"))
print(solution("}]()[{"))
print(solution("[)(]"))
print(solution("}}}"))