# 문자열 관련 함수

# 문자 개수 세기(count)
a = "hobby"
print(a.count('b'))

# 위치 알려주기 1(find)
a = "Python is the best choice"
print(a.find('b'))
print(a.find('k'))

# 위치 알려주기 2(index)
a = "Life is too short"
print(a.index('t'))
#print(a.index('k'))

# 문자열 삽입(join)
print(",".join('abcd'))
print("".join('abcd'))
print(",".join(['a','b','c','d']))
print("".join(['a','b','c','d']))

# 소문자를 대문자로 바꾸기
a = "hi"
print(a.upper())

# 대문자를 소문자로 바꾸기
a = "HI"
print(a.lower())

# 왼쪽 공백 지우기(lstrip)
a = " hi "
print(a.lstrip())

# 오른쪽 공백 지우기(rstrip)
a = " hi "
print(a.rstrip())

# 양쪽 공백 지우기(strip)
a = " hi "
print(a.strip())

# 문자열 바꾸기(replace)
a = "Life is too short"
print(a.replace("Life is" , "Your leg")) # replace(바뀌게 될 문자열, 바꿀 문자열)

# 문자열 나누기(split)
a = "Life is too short"
print(a.split())

b = "a:b:c:d"
print(b.split(':'))