import sys
stack = []
n = int(sys.stdin.readline())

for i in range(n):
    value = sys.stdin.readline().split()
    if value[0] == "push":
        stack.append(value[1])

    elif value[0] == "pop":
        if len(stack):
            print(stack.pop())

        else:
            print(-1)
    elif value[0] == "size":
        print(len(stack))

    elif value[0] == "empty":
        if len(stack):
            print(0)
        else:
            print(1)
    elif value[0] == "top":
        if len(stack):
            print(stack[-1])
        else:
            print(-1)
