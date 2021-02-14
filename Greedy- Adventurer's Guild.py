n = int(input())
data = list(map(int, input().split())) # 공포도 # 2 3 1 2 2

data.sort() # 1 2 2 2 3
result = 0 # 결성된 그룹 수
count = 0  # 현재 그룹 멤버 수

for i in data:
    count += 1
    if count >= i:
        result += 1
        count = 0

print(result)