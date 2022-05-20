n = int(input())

stack = []
answer = 0

for _ in range(n):
    x, y = map(int, input().split())

    if not stack or stack[-1] < y:
        stack.append(y)

    else:
        while stack and stack[-1] > y:
            stack.pop()
            answer += 1

        if not stack or stack[-1] < y:
            stack.append(y)

    if stack[-1] == 0:
        stack.pop()

if stack:
    answer += len(stack)

print(answer)

