from collections import deque

def GCD(n1, n2):
    while n1 * n2 != 0:
        if n1 > n2:
            n1 %= n2
        else:
            n2 %= n1
    return n1 + n2
def solution(arr):
    queue = deque(arr)
    while len(queue) > 1:
        a = queue.popleft()
        b = queue.popleft()
        queue.append((a * b) // GCD(a, b))

    return queue[0]

print(solution([2, 6, 8, 14]))
print(solution([1, 2, 3]))
