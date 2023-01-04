from collections import deque

n, k = map(int, input().split())
queue = deque(range(1, n+1))

cur = 1
print('<', end='')
while len(queue) > 1:
    if cur == k:
        print(queue.popleft(), end=', ')
        cur = 1
    else:
        queue.append(queue.popleft())
        cur += 1

print(queue.pop(), end='>')

