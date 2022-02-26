s = input()

count0 = 0 #0으로 바꾸는 비용
count1 = 0 #1로 바꾸는 비용

if s[0] == '1':
    count0 += 1
else:
    count1 += 1

for i in range(len(s)-1):
    if s[i] != s[i+1]:
        if s[i+1] == '1': #다음 수에서 1로 바뀌는 경우는
            count0 += 1 #0으로 다시 바꿈
        else: #다음 수에서 0으로 바뀌는 경우는
            count1 += 1 #1로 다시 바꿈

print(min(count0, count1))
