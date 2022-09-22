from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    queue = deque()
    queue.append(n)
    while queue:
        x = queue.popleft()
        if x == k:
            print(time[x])
            break
        for i in (x-1, x+1, 2*x):
            if 0 <= i <= 100000 and not time[i]:
                time[i] = time[x] + 1
                queue.append(i)

n, k = map(int, input().split())
time = [0] * 100001
bfs()