'''
lambda
lambda는 함수를 생성할 때 사용하는 예약어로 def와 동일한 역할을 한다.
보통 함수를 한줄로 간결하게 만들 때 사용한다.

사용법
lambda 매개변수1, 매개변수2, ... : 매개변수를 사용한 표현식
'''

add = lambda a, b : a+b
result = add(3,4) # lambda 예약어로 만든 함수는 return 명령어가 없어도 결괏값을 돌려준다.
print(result)