# 사용자 입력

a = input() # input은 입력되는 모든 것을 문자열로 취급한다.
print(a)

number = input("숫자를 입력하세요: ") # input() 괄호 안에 질문 입력
print(number)

# print 자세히 알기

a = 123
print(a) # 숫자 출력

a = "python"
print(a) # 문자열 출력

a = [1,2,3]
print(a) # 리스트 출력

# 큰따옴표(")로 둘러싸인 문자열은 + 연산과 동일하다
print("life" "is" "too short")
print("life"+"is"+"too short")

# 문자열 띄어쓰기는 콤마로 한다.
print("life","is",'too short')

# 한 줄에 결괏값 출력하기
for i in range(10):
    print(i, end=' ')