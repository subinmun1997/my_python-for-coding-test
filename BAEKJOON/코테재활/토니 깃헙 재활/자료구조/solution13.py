ps = input()

stack = []
value = 1
answer = 0

for i in range(len(ps)):
    if ps[i] == '(':
        stack.append(ps[i])
        value *= 2
    elif ps[i] == '[':
        stack.append(ps[i])
        value *= 3
    elif ps[i] == ')':
        if not stack or stack[-1] == '[':
            answer = 0
            break
        if ps[i-1] == '(':
            answer += value
        stack.pop()
        value //= 2
    else:
        if not stack or stack[-1] == '(':
            answer = 0
            break
        if ps[i-1] == '[':
            answer += value
        stack.pop()
        value //= 3

if stack:
    print(0)
else:
    print(answer)