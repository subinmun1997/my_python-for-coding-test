from collections import deque

n, k = map(int, input().split())
queue = deque(i for i in range(1, n+1))

cnt = 1
print('<', end='')
while len(queue) > 1:
    if cnt == k:
        print(queue.popleft(), end=', ')
        cnt = 1
    else:
        queue.append(queue.popleft())
        cnt += 1

print(queue.pop(), end='>')
