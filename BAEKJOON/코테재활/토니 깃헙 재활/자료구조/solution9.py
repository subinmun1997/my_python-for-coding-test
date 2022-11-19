n = int(input())
data = input()
number = [int(input()) for _ in range(n)]

op = {}
for i in range(n):
    op[chr(65+i)] = number[i]

stack = []
for i in data:
    if i.isalpha():
        stack.append(op[i])
    elif i == '*':
        a = stack.pop()
        b = stack.pop()
        stack.append(a*b)
    elif i == '+':
        a = stack.pop()
        b = stack.pop()
        stack.append(a+b)
    elif i == '/':
        a = stack.pop()
        b = stack.pop()
        stack.append(b/a)
    elif i == '-':
        a = stack.pop()
        b = stack.pop()
        stack.append(b-a)

print(f"{sum(stack):.2f}")