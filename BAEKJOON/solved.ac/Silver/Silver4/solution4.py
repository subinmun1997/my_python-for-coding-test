t = int(input())

for _ in range(t):
    stack = []
    flag = True

    ps = input()
    for i in ps:
        if i == '(':
            stack.append(i)
        else:
            if stack:
                stack.pop()
            else:
                flag = False

    if flag and not stack:
        print("YES")
    else:
        print("NO")