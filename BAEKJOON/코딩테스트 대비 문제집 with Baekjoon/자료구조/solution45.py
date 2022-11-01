while True:
    word = input()
    if word == '.':
        break

    stack = []
    for i in word:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                print("no")
                break
        elif i == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                print("no")
                break
    else:
        if not stack:
            print("yes")
        else:
            print("no")

