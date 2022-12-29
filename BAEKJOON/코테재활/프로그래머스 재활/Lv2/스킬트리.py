from collections import deque

def solution(skill, skill_trees):
    answer = 0

    for st in skill_trees:
        skill_queue = deque(skill)
        trees_queue = deque(st)

        for s in st:
            if s not in skill_queue:
                trees_queue.popleft()
            elif s == skill_queue[0]:
                skill_queue.popleft()
                trees_queue.popleft()
            else:
                break
        else:
            answer += 1

    return answer

print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))