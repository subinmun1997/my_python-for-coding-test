def solution(s):
    stack = []
    for i in s:
        if not stack or stack[-1] != i:
            stack.append(i)
        else:
            stack.pop()

    return 0 if stack else 1

print(solution("baabaa"))
print(solution("cdcd"))