from collections import deque

n = int(input())
order = deque(list(map(int, input().split())))
after = deque(range(1, n+1))
before = deque()

while order:
    x = order.pop()
    a = after.popleft()
    if x == 1:
        before.appendleft(a)
    elif x == 2:
        before.insert(1, a)
    elif x == 3:
        before.append(a)

print(*before)

