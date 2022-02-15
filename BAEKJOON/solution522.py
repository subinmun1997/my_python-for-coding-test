n = int(input())

good_word = 0
for _ in range(n):
    s = input()
    stack = []

    for i in range(len(s)):
        if stack and s[i] == stack[-1]:
            stack.pop()
        else:
            stack.append(s[i])

    if not stack:
        good_word += 1

print(good_word)