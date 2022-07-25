from collections import deque

n, m = map(int, input().split())
queue = deque([i for i in range(1, n+1)])
pos = list(map(int, input().split()))

count = 0
for i in pos:
    idx = queue.index(i)
    if idx < len(queue) - idx:
        while True:
            if queue[0] == i:
                queue.popleft()
                break
            else:
                queue.append(queue.popleft())
                count += 1
    else:
        while True:
            if queue[0] == i:
                queue.popleft()
                break
            else:
                queue.appendleft(queue.pop())
                count += 1

print(count)