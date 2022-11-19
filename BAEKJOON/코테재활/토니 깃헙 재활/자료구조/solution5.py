from collections import deque

n, k = map(int, input().split())
queue = deque(i for i in range(1, n+1))

num = 1
print('<', end='')
while len(queue) > 1:
    if num == k:
        print(queue.popleft(), end=', ')
        num = 1
    else:
        queue.append(queue.popleft())
        num += 1

print(queue.pop(), end='>')