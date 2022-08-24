n = int(input())
arr = [int(input()) for _ in range(n)]

start = 1
stack = []
result = []
for i in arr:
    while start <= i:
        result.append('+')
        stack.append(start)
        start += 1
    if stack and stack[-1] == i:
        result.append('-')
        stack.pop()
    else:
        break

if len(stack) > 1:
    print("NO")
else:
    for i in result:
        print(i)

