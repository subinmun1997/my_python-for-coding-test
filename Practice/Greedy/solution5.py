n, m = map(int, input().split())

result = 0
# 한 줄씩 입력받아 확인
for i in range(n):
    data = list(map(int, input().split()))
    # 현재 줄에서 '가장 작은 수' 찾기
    tmp = min(data)
    # '가장 작은 수'들 중에서 가장 큰 수 찾기
    result = max(tmp, result)

print(result)

'''
아이디어: 각 행마다 가장 작은 수를 찾은 뒤에 그 수 중에서 가장 큰 수를 찾는 것
'''