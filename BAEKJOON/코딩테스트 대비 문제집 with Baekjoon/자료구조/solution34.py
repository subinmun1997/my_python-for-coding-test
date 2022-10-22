from collections import deque

n = int(input())

queue = deque()
for _ in range(n):
    data = input().split()
    if data[0] == "push_front":
        queue.appendleft(data[1])
    elif data[0] == "push_back":
        queue.append(data[1])
    elif data[0] == "pop_front":
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif data[0] == "pop_back":
        if queue:
            print(queue.pop())
        else:
            print(-1)
    elif data[0] == "size":
        print(len(queue))
    elif data[0] == "empty":
        if queue:
            print(0)
        else:
            print(1)
    elif data[0] == "front":
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif data[0] == "back":
        if queue:
            print(queue[-1])
        else:
            print(-1)

