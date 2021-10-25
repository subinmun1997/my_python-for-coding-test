n = int(input())
data = list(map(int, input().split()))
data.sort()

team = 0
count = 0

for d in data:
    count += 1
    if count >= d:
        team += 1
        count = 0

print(team)

'''
현재 그룹에 포함된 모험가의 수가 현재 확인하고 있는 공포도보다 크거나 같다면, 이를 그릅으로 설정하면 된다.
'''