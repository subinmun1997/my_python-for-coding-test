n = int(input())
arr = [int(input()) for _ in range(n)]

num = 1
stack = []
answer = []
for ar in arr:
    while num <= ar:
        answer.append('+')
        stack.append(num)
        num += 1
    if stack[-1] == ar:
        answer.append('-')
        stack.pop()
    else:
        print("NO")
        break
else:
    for i in answer:
        print(i)

