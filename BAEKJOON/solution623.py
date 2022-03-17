from collections import deque

n = int(input())
drink = deque(sorted(list(map(int, input().split())), reverse=True))

while len(drink) != 1:
    a = drink.popleft()
    b = drink.popleft()
    if a > b:
        a += b/2
        drink.appendleft(a)
    else:
        b += a/2
        drink.appendleft(b)

print(*drink)