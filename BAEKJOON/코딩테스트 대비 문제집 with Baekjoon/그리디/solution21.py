import sys
input = sys.stdin.readline

'''
마을에 있는 사람들의 수를 순차적으로 더해서 마을 당 인구의 누적 합이 
총 인구 수의 절반 이상이 될 때 그 마을에 우체국을 세우는 것이 해답
'''
pos = []
cnt = 0
n = int(input())
for _ in range(n):
    v, num = map(int, input().split())
    pos.append([v, num])
    cnt += num

pos.sort(key=lambda x : x[0])

answer = 0
total = 0
for i in range(n):
    total += pos[i][1]
    if total >= cnt/2:
        answer = pos[i][0]
        break

print(answer)