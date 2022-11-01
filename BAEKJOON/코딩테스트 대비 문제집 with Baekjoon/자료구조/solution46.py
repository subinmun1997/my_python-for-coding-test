n = int(input())
answer = 0

for _ in range(n):
    word = input()

    stack = []
    for w in word:
        if not stack:
            stack.append(w)
        else:
            if stack[-1] == w:
                stack.pop()
            else:
                stack.append(w)

    if not stack:
        answer += 1

print(answer)