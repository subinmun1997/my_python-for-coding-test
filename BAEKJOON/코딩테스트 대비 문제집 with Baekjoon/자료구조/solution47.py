from collections import deque

n, m = map(int, input().split())
seq = list(map(int, input().split()))

queue = deque([i for i in range(1, n+1)])
answer = 0
for i in seq:
    if queue[0] == i:
        queue.popleft()
    else:
        left = queue.index(i)
        right = len(queue) - queue.index(i)
        if left <= right: #왼>오 이동
            while queue[0] != i:
                queue.append(queue.popleft())
            queue.popleft()
            answer += left
        else:
            #오>왼 이동
            while queue[0] != i:
                queue.appendleft(queue.pop())
            queue.popleft()
            answer += right

print(answer)
