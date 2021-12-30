s = input()

count0 = 0 # 0으로 바꾸기
count1 = 0 # 1로 바꾸기

if s[0] == '0':
    count1 += 1
else:
    count0 += 1

for i in range(1, len(s)):
    if s[i-1] != s[i]:
        if s[i] == '0':
            count1 += 1
        else:
            count0 += 1

print(min(count0, count1))