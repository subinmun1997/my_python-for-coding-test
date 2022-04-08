import sys
from collections import deque

n = int(input())
input = sys.stdin.readline
queue = deque(enumerate(map(int, input().split())))
answer = []

while queue:
    x, y = queue.popleft()
    answer.append(x+1)
    if y > 0:
        queue.rotate(-(y-1))
    else:
        queue.rotate(-y)

print(*answer)