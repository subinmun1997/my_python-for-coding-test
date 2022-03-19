import sys
from collections import deque

def changeRow(array, num):
    start = num * 4
    for i in range(4):
        array[start], array[start + i] = array[start + i], array[start]
    return array

def changeCol(array, num):
    for i in range(4):
        array[num], array[num + i * 4] = array[num + i * 4], array[num]
    return array

def bfs(start, finish):
    queue = deque()
    start = "".join(start)
    finish = "".join(finish)

    queue.append((finish, -1))
    queue.append((start, 1))

    past[start] = (1,None,None,None,None)
    past[finish] = (-1,None,None,None,None)

    while queue:
        now, level = queue.popleft()

        if level > 0:
            next_level = level + 1
        else:
            next_level = level - 1

        next = list(now)

        for idx, func in enumerate([changeRow, changeCol], start=1):

            for i in range(4):
                for k in range(4):
                    next = func(next, i)
                    key = "".join(next)

                    # 처음 발견한 수열이면 정보를 저장.
                    if past.get(key) is None:
                        past[key] = (next_level, now, idx, i+1, k+1) # parent, i, k
                        queue.append((key, next_level))

                    # 두 BFS가 만난다면(이미 발견한 수열인데 깊이의 부호가 다름) 최단 경로를 찾은 것이므로 리턴
                    else:
                        length = abs(past[key][0]) + abs(level) - 1
                        if (past[key][0] < 0 and level > 0) :
                            return now, (idx, i+1, k+1), key, length
                        elif (past[key][0] > 0 and level < 0) :
                            return key, (idx, i+1, 4-(k+1)), now, length

past = {}
square = []
finish = [str(i) for i in range(1, 17)]

for _ in range(4):
    square.extend(list(map(str, sys.stdin.readline().rstrip().split())))

# 10진수 -> 16진수
mapper = {str(i):chr(64+i) for i in range(1,17)}
finish = [mapper[num] for num in finish]
square = [mapper[num] for num in square]

start,center,end,length = bfs(square, finish)

print(length)
answer = []

# 시작 수열에서 시작한 BFS에서 나온 경로
while past.get(start) :
    level, next, rc, i, k = past[start]
    if next is not None :
        answer.append((rc, i, k))
        start = next
    else :
        break
answer = list(reversed(answer))

# 두 BFS가 만난 시점의 경로
answer.append((center[0], center[1], center[2]))

# 정렬된 수열에서 시작한 BFS에서 나온 경로
while past.get(end) :
    level, next, rc, i, k = past[end]
    if next is not None :
        answer.append((rc, i, 4-k))
        end = next
    else :
        break

for ans in answer :
    print(ans[0], ans[1], ans[2])