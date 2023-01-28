from collections import deque

def check_right(start, dir):
    if start > 4 or t[start-1][2] == t[start][6]:
        return
    if t[start-1][2] != t[start][6]:
        check_right(start+1, -dir)
        t[start].rotate(dir)

def check_left(start, dir):
    if start < 1 or t[start][2] == t[start+1][6]:
        return
    if t[start+1][6] != t[start][2]:
        check_left(start-1, -dir)
        t[start].rotate(dir)

t = [deque()]
for i in range(1, 5):
    t.append(deque(list(map(int, input()))))
n = int(input())

for _ in range(n):
    num, dir = map(int, input().split())
    check_right(num+1, -dir)
    check_left(num-1, -dir)
    t[num].rotate(dir)

result = 0
for i in range(4):
    result += (2**i) * t[i+1][0]

print(result)