while True:
    word = input()
    ps = []

    if word == '.':
        break

    for i in word:
        if i == '(' or i == '[':
            ps.append(i)
        elif i == ')':
            if not ps or ps[-1] == '[':
                print("no")
                break
            ps.pop()
        elif i == ']':
            if not ps or ps[-1] == '(':
                print("no")
                break
            ps.pop()

    else:
        if ps:
            print("no")
        else:
            print("yes")
