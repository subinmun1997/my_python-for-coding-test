n = int(input())
arr = [int(input()) for _ in range(n)]

num = 1
stack = []
answer = []
for i in arr:
    while num <= i:
        answer.append('+')
        stack.append(num)
        num += 1
    if stack[-1] == i:
        answer.append('-')
        stack.pop()
    else:
        print("NO")
        exit()

for i in answer:
    print(i)
