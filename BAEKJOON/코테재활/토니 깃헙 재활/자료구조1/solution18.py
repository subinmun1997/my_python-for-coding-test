while True:
    order = input()
    if order == '.':
        break

    stack = []
    for i in order:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if not stack or stack[-1] == '[':
                print("no")
                break
            else:
                stack.pop()
        elif i == ']':
            if not stack or stack[-1] == '(':
                print("no")
                break
            else:
                stack.pop()
    else:
        if stack:
            print("no")
        else:
            print("yes")
