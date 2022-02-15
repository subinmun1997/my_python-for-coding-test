s = input()

count = 0
stack = []
for i in range(len(s)):
    if s[i] == '(':
        stack.append(s[i])
    elif s[i] == ')':
        if not stack or stack[-1] != '(':
            stack.append(s[i])
        elif stack[-1] == '(':
            stack.pop()
            count += 1

print(len(s) - count*2)