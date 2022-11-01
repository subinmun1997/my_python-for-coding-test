from collections import deque

n = int(input())
card = list(map(int, input().split()))
after = deque(i for i in range(1, n+1))
before = deque()

while card:
    x = card.pop()
    a = after.popleft()
    if x == 1:
        before.appendleft(a)
    elif x == 2:
        before.insert(1, a)
    elif x == 3:
        before.append(a)

print(*before)
