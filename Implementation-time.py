h = int(input())

count = 0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i)+str(j)+str(k): # 매 시각을 문자열로 바꾼 다음 문자열에 '3'이 포함됐는지 검사
                count+=1

print(count)
