import sys
from collections import deque
input = sys.stdin.readline


def bfs():
    queue = deque()
    queue.append(n)
    while queue:
        x = queue.popleft()
        if x == k:
            print(time[x])
            break
        for j in (x-1, x+1, x*2):
            if 0 <= j <= 100000 and not time[j]:
                time[j] = time[x] + 1
                queue.append(j)


n, k = map(int, input().split())
time = [0] * (100001)
bfs()