n = int(input())

count = 0
for _ in range(n):
    word = input()
    stack = []
    for w in word:
        if not stack or stack[-1] != w:
            stack.append(w)
        elif stack[-1] == w:
            stack.pop()

    if not stack:
        count += 1

print(count)
