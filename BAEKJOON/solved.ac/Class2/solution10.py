from collections import deque

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    priority = deque(list(map(int, input().split())))
    check = [False] * n
    check[m] = True

    count = 1
    while True:
        if priority[0] == max(priority) and check[0]:
            print(count)
            break
        elif priority[0] == max(priority):
            priority.popleft()
            check.pop(0)
            count += 1
        else:
            priority.append(priority.popleft())
            check.append(check.pop(0))
