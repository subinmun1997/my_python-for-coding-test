from collections import deque

def solution(arr):
    queue = deque(arr)
    while len(queue) != 1:
        a = queue.popleft()
        b = queue.popleft()
        queue.appendleft(a * b // gcd(a, b))

    return queue[0]

def gcd(a, b):
    while a*b != 0:
        if a > b:
            a %= b
        else:
            b %= a

    return a+b

print(solution([2, 6, 8, 14]))
print(solution([1, 2, 3]))