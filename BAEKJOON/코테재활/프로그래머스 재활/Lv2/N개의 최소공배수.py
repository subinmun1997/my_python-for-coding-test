import math
from collections import deque

def solution(arr):
    queue = deque(arr)
    while len(queue) != 1:
        a = queue.popleft()
        b = queue.popleft()
        queue.append(a * b // math.gcd(a, b))

    return queue[0]

print(solution([2,6,8,14]))
print(solution([1,2,3]))