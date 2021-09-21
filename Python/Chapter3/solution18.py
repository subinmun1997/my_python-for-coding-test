'''
for문과 함께 자주 사용하는 range 함수

for문은 숫자 리스트를 자동으로 만들어 주는 range 함수와 함께 사용하는 경우가 많다.
'''

# 예시 1
a = range(10)
print(a)

# 예시 2
add = 0
for i in range(1,11):
    add += i

print(add)

# 예시 3
marks = [90,25,67,45,80]

for number in range(len(marks)):
    if marks[number] < 60 : continue
    print("%d번 학생 축하합니다. 합격입니다." %(number+1))

# 예시 4
for i in range(2,10):
    for j in range(1,10):
        print(i*j, end=' ')
    print('')