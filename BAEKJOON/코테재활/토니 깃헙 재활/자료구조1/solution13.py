ps = input()

answer = 0
temp = 1
stack = []

for i in range(len(ps)):
    if ps[i] == '(':
        stack.append(ps[i])
        temp *= 2
    elif ps[i] == '[':
        stack.append(ps[i])
        temp *= 3
    elif ps[i] == ')':
        if not stack or stack[-1] == '[':
            answer = 0
            break
        elif ps[i-1] == '(':
            answer += temp
        temp //= 2
        stack.pop()
    elif ps[i] == ']':
        if not stack or stack[-1] == '(':
            answer = 0
            break
        elif ps[i-1] == '[':
            answer += temp
        temp //= 3
        stack.pop()

if stack:
    print(0)
else:
    print(answer)