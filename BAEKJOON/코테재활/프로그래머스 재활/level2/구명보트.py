from collections import deque

def solution(people, limit):
    people = deque(sorted(people, reverse=True))
    count = 0

    while people:
        if len(people) >= 2 and people[0] + people[-1] <= limit:
            people.popleft()
            people.pop()
        else:
            people.popleft()
        count += 1

    return count

print(solution([70, 50, 80, 50], 100))
print(solution([70, 80, 50], 100))