n,m = map(int,input().split())

result = 0

for i in range(n):
    data = list(map(int,input().split()))
    min_value = 100 # 각 행의 min_value와 비교하기 위한 임의의 값
    for a in data: # 행의 값을 하나씩 가져옴
        min_value = min(min_value,a) #위의 min_value와 행에서의 가장 작은 값 비교
    result = max(result,min_value) # result: '전' 행의 min_value값과 '현' 행의 min_value 값 비교

print(result)