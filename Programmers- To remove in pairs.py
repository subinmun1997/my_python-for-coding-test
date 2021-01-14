def solution(s):
    stack = []
    for i in s:
        stack.append(i)
        while True:
            if len(stack) >= 2:
                if stack[-1] == stack[-2]:
                    stack.pop()
                    stack.pop()
                else:
                    break
            else:
                break
    return not stack
