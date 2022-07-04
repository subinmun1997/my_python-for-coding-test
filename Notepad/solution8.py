s = input()

count0 = 0 #0으로 뒤집기
count1 = 0 #1로 뒤집기

# 첫번째 값에 대한 처리
if s[0] == '1':
    count0 += 1
else:
    count1 += 1

for i in range(1, len(s)):
    if s[i] != s[i-1]:
        if s[i] == '1':
            count0 += 1
        else:
            count1 += 1

print(min(count0, count1))