from collections import deque

n, k = map(int, input().split())
queue = deque([i for i in range(1, n+1)])
count = 1

print("<", end='')
while len(queue) != 1:
    if count != k:
        queue.append(queue.popleft())
        count += 1
    else:
        print(queue.popleft(), end=', ')
        count = 1

print(queue.popleft(), end='>')