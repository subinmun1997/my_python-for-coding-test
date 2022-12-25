from collections import deque

def solution(s):
    answer = 0
    queue = deque(s)
    for i in range(len(queue)):
        if check_paren(queue):
            answer += 1
        queue.append(queue.popleft())
    return answer

def check_paren(data):
    stack = []
    for i in data:
        if i in ['[','(','{']:
            stack.append(i)
        elif i == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                return False
        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                return False
        elif i == '}':
            if stack and stack[-1] == '{':
                stack.pop()
            else:
                return False
    if stack:
        return False
    else:
        return True

print(solution("[](){}"))
print(solution("}]()[{"))
print(solution("[)(]"))
print(solution("}}}"))