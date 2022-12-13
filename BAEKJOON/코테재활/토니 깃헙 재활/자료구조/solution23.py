from collections import deque

t = int(input())
for _ in range(t):
    p = input()
    n = int(input())
    data = input()[1:-1].split(',')
    arr = deque(data)

    flag = 0

    if n == 0:
        arr = deque()

    for i in p:
        if i == 'R':
            flag += 1
        else:
            if len(arr) == 0:
                print("error")
                break
            else:
                if flag % 2 == 0:
                    arr.popleft()
                else:
                    arr.pop()

    else:
        if flag % 2 == 0:
            print('[' + ','.join(arr) + ']')
        else:
            arr.reverse()
            print('[' + ','.join(arr) + ']')