n = int(input())
s = input()

numbers = [int(input()) for _ in range(n)]

stack = []
for i in s:
    if i.isalpha():
        stack.append(numbers[int(ord(i)) - int(ord('A'))])
    elif i == "*":
        a = stack.pop()
        b = stack.pop()
        stack.append(a*b)
    elif i == "+":
        a = stack.pop()
        b = stack.pop()
        stack.append(a+b)
    elif i == '-':
        a = stack.pop()
        b = stack.pop()
        stack.append(b-a)
    elif i == '/':
        a = stack.pop()
        b = stack.pop()
        stack.append(b/a)

print(f"{sum(stack):.2f}")

