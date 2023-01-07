order = input()

op1 = ['+', '-']
op2 = ['*', '/']

stack = []
result = []

for i in order:
    if i.isalpha():
        result.append(i)
    elif i in op1:
        if not stack:
            stack.append(i)
        else:
            while stack and stack[-1] in op1+op2:
                result.append(stack.pop())
            stack.append(i)
    elif i in op2:
        if not stack:
            stack.append(i)
        else:
            while stack and stack[-1] in op2:
                result.append(stack.pop())
            stack.append(i)
    elif i == '(':
        stack.append(i)
    elif i == ')':
        while stack and stack[-1] != '(':
            result.append(stack.pop())
        stack.pop()

while stack:
    result.append(stack.pop())

print(''.join(result))