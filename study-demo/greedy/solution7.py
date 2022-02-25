n = int(input())
data = sorted(list(map(int, input().split())))
group = 0 # 총 그룹의 수

count = 0 # 현재 그룹에 포함된 모험가의 수
for d in data:
    count += 1
    if d <= count:
        group += 1
        count = 0

print(group)