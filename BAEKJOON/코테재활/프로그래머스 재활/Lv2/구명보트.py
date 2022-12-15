from collections import deque

def solution(people, limit):
    answer = 0
    queue = deque(sorted(people, reverse=True))
    while queue:
        if len(queue) >= 2 and queue[0] + queue[-1] <= limit:
            queue.popleft()
            queue.pop()
        else:
            queue.popleft()
        answer += 1

    return answer

print(solution([70, 50, 80, 50], 100))
print(solution([70, 80, 50], 100))