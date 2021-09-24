k = int(input())

stack = []
data = [int(input()) for _ in range(k)]
for i in data:
    if i != 0:
        stack.append(i)
    else:
        stack.pop()

print(sum(stack))