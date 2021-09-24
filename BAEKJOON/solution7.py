n = int(input())

def check(a):
    stack = []
    for k in a:
        if k == '(':
            stack.append(k)
        elif k == ')':
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

for i in range(n):
    a = list(input())
    check(a)

