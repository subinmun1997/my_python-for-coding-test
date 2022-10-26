laser = input()

stack = []
answer = 0
for i in range(len(laser)):
    if laser[i] == '(':
        stack.append('(')
    else:
        if laser[i-1] == '(':
            stack.pop()
            answer += len(stack)
        else:
            stack.pop()
            answer += 1

print(answer)
