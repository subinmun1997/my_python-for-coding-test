import sys
from collections import deque

N, K, M = map(int,sys.stdin.readline().split())

graph = deque([i for i in range(1,N+1)])

flag = 0
count = 0
switch = 0

for _ in range(N):
  if flag == 0:
    graph.rotate(-K)
    print(graph.pop())
    count += 1

  else:
    graph.rotate(K-1)
    print(graph.pop())
    count += 1

  if count == M and switch==0:
    flag = 1
    count = 0
    switch = 1
  elif count==M and switch==1:
    flag = 0
    count = 0
    switch = 0