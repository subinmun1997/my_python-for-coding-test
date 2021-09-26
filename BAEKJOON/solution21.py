import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
queue = deque()
result = []
count = 1
for i in range(1,n+1):
    queue.append(i)
while len(queue)>0:
    if count != k:
        queue.append(queue.popleft())
        count += 1
    else:
        result.append(queue.popleft())
        count = 1

print("<",end='')
for r in range(len(result)-1):
    print(result[r],end=', ')
print(result[-1],end='>')
