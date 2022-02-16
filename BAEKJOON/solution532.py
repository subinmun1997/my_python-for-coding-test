from collections import deque

n = int(input())
command = deque(map(int, input().split()))
after = deque(range(1, n+1))
before = deque()

while command:
    x = command.pop()
    a = after.popleft()
    if x == 1:
        before.appendleft(a)
    elif x == 2:
        before.insert(1, a)
    elif x == 3:
        before.append(a)

print(*before)