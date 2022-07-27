n = int(input())
arr = [0] + [int(input()) for _ in range(n)]

stack = [0]
idx = 1
answer = []
for i in range(1, n+1):
    while stack[-1] < arr[i]:
        stack.append(idx)
        answer.append('+')
        idx += 1
    stack.pop()
    answer.append('-')

if len(stack) > 1:
    print('NO')
else:
    for i in answer:
        print(i)





