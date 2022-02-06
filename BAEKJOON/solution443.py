n = int(input())

stack = []
for _ in range(n):
    data = list(map(str, input().split()))
    if data[1] == "enter":
        stack.append(data[0])
    else:
        stack.pop(stack.index(data[0]))

stack.sort(reverse=True)
for s in stack:
    print(s)