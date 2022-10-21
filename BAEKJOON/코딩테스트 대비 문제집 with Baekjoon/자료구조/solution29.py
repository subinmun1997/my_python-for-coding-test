n = int(input())
for _ in range(n):
    data = input()
    stack = []

    for i in data:
        if i == '(':
            stack.append(i)
        else:
            if stack:
                stack.pop()
            else:
                print("NO")
                break
    else:
        if stack:
            print("NO")
        else:
            print("YES")