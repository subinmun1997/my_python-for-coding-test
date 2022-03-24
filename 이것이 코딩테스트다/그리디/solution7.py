n = int(input())
values = sorted(list(map(int, input().split())))

group = 0 # 결성된 그룹 수

temp = 0 # 현재 멤버 수
for i in values:
    temp += 1
    if temp >= i:
        group += 1
        temp = 0

print(group)