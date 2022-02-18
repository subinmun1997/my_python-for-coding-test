razor = input()
answer = 0
stack = []

for i in range(len(razor)):
    if razor[i] == '(':
        stack.append('(')

    else:
        if razor[i-1] == '(':
            stack.pop()
            answer += len(stack)
        else:
            stack.pop()
            answer += 1

print(answer)