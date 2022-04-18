while True:
    stack = []
    flag = True
    words = input()
    if words == '.':
        break
    for word in words:
        if word == '(' or word == '[':
            stack.append(word)
        elif word == ')':
            if not stack or stack[-1] == '[':
                flag = False
                break
            elif stack[-1] == '(':
                stack.pop()
        elif word == ']':
            if not stack or stack[-1] == '(':
                flag = False
                break
            elif stack[-1] == '[':
                stack.pop()

    if not stack and flag:
        print("yes")
    else:
        print("no")
