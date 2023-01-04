def check_ps(ps):
    stack = []
    for p in ps:
        if p == '(':
            stack.append(p)
        else:
            if not stack:
                return False
            stack.pop()

    if stack:
        return False
    else:
        return True

t = int(input())
for _ in range(t):
    ps = input()
    if check_ps(ps):
        print("YES")
    else:
        print("NO")