# 리스트 자료형
odd = [1,3,5,7,9]
print(odd)

a = []
b = [1,2,3]
c = ['Life','is','too','short']
d = [1,2,'Life','is']
e = [1,2,['Life','is']] # e처럼 리스트 자체를 요소로 가질 수 있다.

# 리스트의 인덱싱과 슬라이싱
# 리스트의 인덱싱

a = [1,2,3]
print(a)
print(a[0])
print(a[0]+a[2])
print(a[-1])

a = [1,2,3,['a','b','c']]
print(a[0])
print(a[-1])
print(a[3])
print(a[3][0])
print(a[-1][0])
print(a[-1][1])
print(a[-1][2])

# 삼중 리스트에서 인덱싱하기
a = [1,2,['a','b',['Life','is']]]
print(a[2])
print(a[2][2])
print(a[2][2][0])

# 리스트의 슬라이싱
a = [1,2,3,4,5]
print(a[0:2])

# 문자열의 슬라이싱
a = "12345"
print(a[0:2])

a = [1,2,3,4,5]
print(a[:2])
print(a[2:])

# 중첩된 리스트에서 슬라이싱하기
a = [1,2,3,['a','b','c'],4,5]
print(a)
print(a[2:5])
print(a[3][:2])