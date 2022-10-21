import sys
input = sys.stdin.readline

n = int(input())

stack = []
for _ in range(n):
    data = input().split()
    if data[0] == "push":
        stack.append(data[1])
    elif data[0] == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)
    elif data[0] == "pop":
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif data[0] == "size":
        print(len(stack))
    elif data[0] == "empty":
        if stack:
            print(0)
        else:
            print(1)