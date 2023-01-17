import math

n = int(input())
candidate = list(map(int, input().split()))
b, c = map(int, input().split())

answer = 0
for cand in candidate:
    if cand <= b:
        answer += 1
    else:
        answer += math.ceil((cand - b) / c) + 1

print(answer)
