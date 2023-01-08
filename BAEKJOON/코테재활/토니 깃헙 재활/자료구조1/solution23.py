from collections import deque

t = int(input())
for _ in range(t):
    p = input()
    n = int(input())
    arr = deque(input()[1:-1].split(','))

    if n == 0:
        arr = []

    countr = 0
    for i in p:
        if i == 'R':
            countr += 1
        else:
            if len(arr) == 0:
                print("error")
                break
            else:
                if countr % 2 == 0:
                    arr.popleft()
                else:
                    arr.pop()
    else:
        if countr % 2 == 0:
            print('[' + ','.join(arr) + ']')
        else:
            arr.reverse()
            print('[' + ','.join(arr) + ']')