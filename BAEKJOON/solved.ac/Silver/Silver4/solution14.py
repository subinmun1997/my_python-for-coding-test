from collections import deque

n, k = map(int, input().split())
queue = deque(i for i in range(1, n+1))

cnt = 1
print('<', end='')
while len(queue) > 1:
    if cnt != k:
        queue.append(queue.popleft())
        cnt += 1
    else:
        print(queue.popleft(), end=', ')
        cnt = 1

print(queue.popleft(), end='>')