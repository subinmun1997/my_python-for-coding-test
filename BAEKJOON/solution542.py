n = int(input())
score = 0

stack = []
for _ in range(n):
    hw = list(map(int, input().split()))
    if hw[0] == 1:
        if hw[2]-1 == 0:
            score += hw[1]
        else:
            stack.append([hw[1], hw[2]-1])
    else:
        if stack:
            t = stack.pop()
            t[1] -= 1
            if t[1] == 0:
                score += t[0]
            else:
                stack.append(t)
print(score)