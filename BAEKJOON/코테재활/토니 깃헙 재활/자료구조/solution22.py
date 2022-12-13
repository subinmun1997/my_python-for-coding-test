from collections import deque

n = int(input())
card = list(map(int, input().split()))
queue = deque(range(1, n+1))

result = deque()
while card:
    x = card.pop()
    a = queue.popleft()

    if x == 1:
        result.appendleft(a)
    elif x == 2:
        result.insert(1, a)
    elif x == 3:
        result.append(a)

print(*result)
