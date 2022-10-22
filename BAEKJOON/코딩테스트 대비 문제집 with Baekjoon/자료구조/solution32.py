from collections import deque

n, k = map(int, input().split())
queue = deque([i for i in range(1, n+1)])

print('<', end='')
idx = 1
while len(queue) != 1:
    if idx == k:
        print(queue.popleft(), end=', ')
        idx = 1
    else:
        idx += 1
        queue.append(queue.popleft())

print(queue.pop(), end='>')