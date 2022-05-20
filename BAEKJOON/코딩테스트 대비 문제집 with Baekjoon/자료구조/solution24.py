from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    p = input().rstrip()
    n = int(input())
    array = input().rstrip()[1:-1].split(',')

    queue = deque(array)
    rev, front, back = 0, 0, len(queue)-1
    flag = 0
    if n == 0:
        queue = []
        front, back = 0, 0

    for i in p:
        if i == 'R':
            rev += 1
        elif i == 'D':
            if len(queue) < 1:
                flag = 1
                print("error")
                break
            else:
                if rev%2 == 0:
                    queue.popleft()
                else:
                    queue.pop()

    if flag == 0:
        if rev%2 == 0:
            print("[" + ",".join(queue) + "]")
        else:
            queue.reverse()
            print("[" + ",".join(queue) + "]")