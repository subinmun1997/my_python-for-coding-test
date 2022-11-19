laser = input()

stack = []
count = 0
for i in range(len(laser)):
    if laser[i] == '(':
        stack.append(laser[i])
    else:
        if laser[i-1] == '(':
            stack.pop()
            count += len(stack)
        else:
            stack.pop()
            count += 1

print(count)
