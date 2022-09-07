t = int(input())

for _ in range(t):
    ps = input()

    flag = True
    stack = []
    for i in ps:
        if i == '(':
            stack.append(i)
        else:
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                flag = False
                break
    if not stack and flag:
        print("YES")
    else:
        print("NO")

