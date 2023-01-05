n = int(input())
data = input()

alphaNum = dict()
for i in range(n):
    num = int(input())
    alphaNum[chr(65 + i)] = num

stack = []
for an in data:
    if an.isalpha():
        stack.append(alphaNum[an])
    elif an == '*':
        a = stack.pop()
        b = stack.pop()
        stack.append(a*b)
    elif an == '+':
        a = stack.pop()
        b = stack.pop()
        stack.append(a+b)
    elif an == '/':
        a = stack.pop()
        b = stack.pop()
        stack.append(b/a)
    elif an == '-':
        a = stack.pop()
        b = stack.pop()
        stack.append(b-a)

print(f'{sum(stack):.2f}')