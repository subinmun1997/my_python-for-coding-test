import sys
input = sys.stdin.readline

n = int(input())
array = []
cnt = 0
for i in range(n):
    v, num = map(int, input().split())
    array.append([v, num])
    cnt += num

array.sort(key=lambda x:x[0])

total = 0
answer = 0
for i in range(n):
    total += array[i][1]
    if total > cnt/2:
        answer = array[i][0]
        break

print(answer)