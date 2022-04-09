from collections import deque

n = int(input())
drink = deque(sorted(list(map(int, input().split())), reverse=True))

while len(drink) != 1:
    a = drink.popleft()
    b = drink.popleft()

    if a > b:
        temp = a + (b/2)
    else:
        temp = b + (a/2)
    drink.appendleft(temp)

print(sum(drink))