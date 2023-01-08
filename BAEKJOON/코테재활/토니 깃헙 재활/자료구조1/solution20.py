from collections import deque

n, m = map(int, input().split())
pos = list(map(int, input().split()))
queue = deque(range(1, n+1))

count = 0
for p in pos:
    if p == queue[0]:
        queue.popleft()
    else:
        cur_idx = queue.index(p)
        if cur_idx < len(queue) - cur_idx:
            while queue[0] != p:
                queue.append(queue.popleft())
                count += 1
        else:
            while queue[0] != p:
                queue.appendleft(queue.pop())
                count += 1
        queue.popleft()

print(count)
