from collections import deque
from math import gcd

def solution(arr):
    queue = deque(arr)
    while len(queue) != 1:
        a = queue.popleft()
        b = queue.popleft()
        result = (a * b // gcd(a, b))
        queue.appendleft(result)

    return queue[0]

print(solution([2,6,8,14]))
print(solution([1,2,3]))