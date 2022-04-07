laser = input()

result = 0
stack = []
for i in range(len(laser)):
    if laser[i] == '(':
        stack.append('(')
    else:
        if laser[i-1] == '(':
            stack.pop()
            result += len(stack)
        else:
            stack.pop()
            result += 1

print(result)