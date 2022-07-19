import sys
input = sys.stdin.readline

n = int(input())

stack = []
for _ in range(n):
    target = input().split()

    if target[0] == "push":
        stack.append(target[1])
    elif target[0] == "pop":
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif target[0] == "size":
        print(len(stack))
    elif target[0] == "empty":
        if stack:
            print(0)
        else:
            print(1)
    elif target[0] == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)