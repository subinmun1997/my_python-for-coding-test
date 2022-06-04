import sys
input = sys.stdin.readline

n, c = map(int, input().split())
m = int(input())
arr = [list(map(int, input().split())) for _ in range(m)]
arr.sort(key=lambda x:x[1])

box = [c] * (n+1)
answer = 0
for s, e, b in arr:
    min_value = c
    for i in range(s, e):
        min_value = min(min_value, box[i])
    min_value = min(min_value, b)
    for i in range(s, e):
        box[i] -= min_value
    answer += min_value

print(answer)