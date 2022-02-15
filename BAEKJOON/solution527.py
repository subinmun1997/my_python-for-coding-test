import sys
input = sys.stdin.readline

from collections import deque

queue = deque()
n = int(input())

for _ in range(n):
    x = input().split()
    if x[0] == "push":
        queue.append(x[1])
    elif x[0] == "pop":
        print(queue.popleft() if queue else -1)
    elif x[0] == "size":
        print(len(queue))
    elif x[0] == "empty":
        print(1 if len(queue)==0 else 0)
    elif x[0] == "front":
        print(queue[0] if queue else -1)
    elif x[0] == "back":
        print(queue[-1] if queue else -1)
