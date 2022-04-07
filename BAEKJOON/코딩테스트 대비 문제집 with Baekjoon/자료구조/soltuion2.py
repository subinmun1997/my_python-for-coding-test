t = int(input())

def check(array):
    stack = []
    for i in array:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if stack:
                stack.pop()
            else:
                print("NO")
                return

    if stack:
        print("NO")
        return
    else:
        print("YES")
        return

for _ in range(t):
    data = list(input())
    check(data)