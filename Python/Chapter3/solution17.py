'''
for문과 continue문

while문에서 살펴본 continue문을 for문에서도 사용할 수 있다.
for문 안의 문장을 수행하는 도중에 continue문을 만나면 for문의 처음으로 돌아가게 된다.
'''

marks = [90,25,67,45,80]

number = 0
for mark in marks:
    number += 1
    if mark < 60: continue
    print("%d번 학생 축하합니다. 합격입니다." %number)