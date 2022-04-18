n = int(input())

result = 0
for _ in range(n):
    word = input()
    stack = []

    for i in range(len(word)):
        if stack and word[i] == stack[-1]:
            stack.pop()
        else:
            stack.append(word[i])

    if not stack:
        result += 1

print(result)