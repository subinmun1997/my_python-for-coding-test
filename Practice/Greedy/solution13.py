s = input()

count0 = 0
count1 = 0

first = s[0]
if first == '0':
    count1 += 1
else:
    count0 += 1

for i in range(len(s)-1):
    if s[i] != s[i+1]:
        if s[i+1] == '0':
            count1 += 1
        else:
            count0 += 1

print(min(count1, count0))

'''
전부 0으로 바꾸는 경우와 전부 1로 바꾸는 경우 중에서 더 적은 횟수를 가지는 경우를 계산하면 된다.
'''