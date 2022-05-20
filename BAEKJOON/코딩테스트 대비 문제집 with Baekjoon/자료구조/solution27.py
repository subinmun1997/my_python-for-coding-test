from sys import stdin

input = stdin.readline

N = int(input())
building = list(map(int, input().split()))
answer = [[0] for _ in range(N)]

stack = []
for i in range(N):
    while stack and stack[-1][1] <= building[i]:
        stack.pop()
    if stack:
        answer[i][0] += len(stack)
        answer[i].append(stack[-1][0])

    stack.append([i, building[i]])
    print(stack, answer)

stack = []
for i in range(N - 1, -1, -1):
    while stack and stack[-1][1] <= building[i]:
        stack.pop()
    if stack:
        answer[i][0] += len(stack)
        if 1 < len(answer[i]):
            if (i - answer[i][1]) > (stack[-1][0] - i):
                answer[i][1] = stack[-1][0]
        else:
            answer[i].append(stack[-1][0])

    stack.append([i, building[i]])

result = []
for i in range(N):
    if 1 < len(answer[i]):
        result.append(f'{answer[i][0]} {answer[i][1] + 1}')
    else:
        result.append('0')

print('\n'.join(result))