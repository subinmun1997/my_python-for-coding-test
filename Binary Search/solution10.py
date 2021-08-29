n, m = map(int, input().split())
array = list(map(int, input().split()))

start = 0
end = max(array)

while start <= end:
    total = 0
    mid = (start + end) // 2

    for i in array:
        if i > mid: # 떡의 길이가 중간값보다 크면 자르고 total에 추가
            total += (i-mid)
    if total < m: # 자른 떡의 길이가 요구하는 길이보다 짧으면 end 값 수정
        end = mid - 1
    else: # 자른 떡의 길이가 요구하는 길이보다 길면 start 값 수정
        result = total
        start = mid + 1

print(result)




