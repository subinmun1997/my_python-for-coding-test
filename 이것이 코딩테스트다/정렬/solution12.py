n = int(input())

array = []
for _ in range(n):
    data = input().split()
    array.append((data[0], int(data[1])))

# 키(Key)를 이용하여 점수를 기준으로 정렬
array.sort(key=lambda x : x[1])
for i in array:
    print(i[0], end=' ')