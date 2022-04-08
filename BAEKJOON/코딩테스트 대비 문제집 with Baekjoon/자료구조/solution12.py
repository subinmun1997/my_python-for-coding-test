braket = list(input())

stack = []
answer = 0
temp = 1

for i in range(len(braket)):
    if braket[i] == '(':
        stack.append(braket[i])
        temp *= 2
    elif braket[i] == '[':
        stack.append(braket[i])
        temp *= 3
    elif braket[i] == ')':
        if not stack or stack[-1] == '[':
            answer = 0
            break
        if braket[i-1] == '(':
            answer += temp
        stack.pop()
        temp //= 2
    else:
        if not stack or stack[-1] == '(':
            answer = 0
            break
        if braket[i-1] == '[':
            answer += temp
        stack.pop()
        temp //= 3

if stack:
    print(0)
else:
    print(answer)