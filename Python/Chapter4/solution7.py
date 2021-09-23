# 매개변수에 초깃값 미리 설정하기
# 함수의 매개변수에 들어갈 값이 항상 변하는 것이 아닐 경우네는 초깃값을 미리 설정해 두면 유용하다.
def say_myself(name, old, man=True): # 매개변수 초깃값을 설정하는 방법
    print("나의 이름은 %s입니다." %name)
    print("나이는 %d살입니다." %old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")

say_myself("박응용", 27)
say_myself("박응용", 27, True)
say_myself("박응선", 27, False)

'''
주의
초깃값을 설정해 놓은 매개변수 뒤에 초깃값을 설정해 놓지 않은 매개변수는 사용할 수 없다.
초기화시키고 싶은 매개변수를 항상 가장 뒤쪽에 놓아야 한다.

# ex
def say_myself2(name, man=True, old): # 오류 발생
    print("나의 이름은 %s입니다." %name)
    print("나이는 %d살입니다." %old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")

say_myself2("박응용", 27)
'''

