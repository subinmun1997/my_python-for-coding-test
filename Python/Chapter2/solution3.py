# 문자열 연산하기

# 문자열 더해서 연결하기
head = "Python"
tail = " is fun! "
print(head + tail)

# 문자열 곱하기
a = "python"
print(a*2)

# 문자열 곱하기 응용
print("=" * 50)
print("My Program")
print("=" * 50)

# 문자열 길이 구하기
a = "Life is too short"
print(len(a))

# 문자열 인덱싱과 슬라이싱

# 문자열 인덱싱
a = "Life is too short, You need python"
print(a[3])

print(a[0])
print(a[12])
print(a[-1]) # 뒤에서 부터 세어 첫 번째
print(a[-0]) # print(a[0])과 동일
print(a[-2])
print(a[-5])

# 문자열 슬라이싱

b = a[0] + a[1] + a[2] + a[3]
print(b)

print(a[0:4])
print(a[0:5])
print(a[0:2])
print(a[5:7])
print(a[12:17])
print(a[19:]) # 끝 번호 생략하면 시작 번호부터 끝까지 출력
print(a[:17]) # 시작 번호 생략하면 문자열의 처음부터 끝 번호까지 출력
print(a[:]) # 시작 번호와 끝 번호를 생략하면 문자열 전체 출력
print(a[19:-7]) # 19부터 -8까지

# 슬라이싱으로 문자열 나누기
a = "20010331Rainy"
date = a[:8]
weather = a[8:]
print(date)
print(weather)

year = a[:4]
day = a[4:8]
weather = a[8:]
print(year)
print(day)
print(weather)