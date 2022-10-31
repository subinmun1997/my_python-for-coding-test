import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
q = deque(enumerate(map(int, input().split())))
answer = []

while q:
    x, y = q.popleft()
    answer.append(x+1)
    if y > 0:
        q.rotate(-(y-1))
    else:
        q.rotate(-y)

print(*answer)

