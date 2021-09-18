# 문자열 포매팅

print("I eat %d apples." %3)
print("I eat %s apples." %"five")

number = 3
print("I eat %d apples." %number)

number = 10
day = "three"
print("I ate %d apples. so I was sick for %s days" %(number,day))

# '%s' 포맷 코드는 어떤 형태의 값이든 변환해 넣을 수 있다.
print("I have %s apples." %3)
print("rate is %s" %3.234)

# 포매팅 연산자 %d와 %를 같이 쓸 때는 %%를 쓴다.
print("Error is %d%%" %98)

# 포맷 코드와 숫자 함께 사용하기
print("%10s" %"Hi")
print("%-10sjane" %"Hi")

# 소수점 표현하기
print("%0.4f" %3.42134234)
print("%10.4f" %3.42134234)

# format 함수를 사용한 포매팅
print("I eat {0} apples".format(3))
print("I eat {0} apples".format("five"))

number = 3
print("I eat {0} apples".format(number))

# 2개 이상의 값 넣기
number = 10
day = "three"
print("I ate {0} apples. so i was sick for {1} days".format(number, day))
print("I ate {number} apples. so i was sick for {day} days".format(number=10, day=3))
print("I ate {0} apples. so I was sick for {day} days".format(10, day=3))

# 왼쪽 정렬
print("{0:<10}".format("hi"))

# 오른쪽 정렬
print("{0:>10}".format("hi"))

# 가운데 정렬
print("{0:^10}".format("hi"))

# 공백 채우기
print("{0:=^10}".format("hi"))
print("{0:!<10}".format("hi"))

# 소수점 표현하기
y = 3.42134234
print("{0:0.4f}".format(y))
print("{0:10.4f}".format(y))

# { 또는 } 문자 표현하기
print("{{ and }}".format())

# f 문자열 포매팅
name = "홍길동"
age = 30
print(f'나의 이름은 {name}입니다. 나이는 {age}입니다.')
print(f'나는 내년이면 {age+1}살이 된다.')

d = {'name' : '홍길동', 'age':30}
print(f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.')