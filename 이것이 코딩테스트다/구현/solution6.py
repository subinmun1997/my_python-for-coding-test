s = input()
number = 0 # 숫자
result = [] # 문자

for i in s:
    if i.isalpha(): # 알파벳인 경우 리스트에 삽입
        result.append(i)
    elif i.isdigit(): # 숫자인 경우 따로 더하기
        number += int(i)

result.sort()
if number != 0: # 숫자가 하나라도 존재한다면 리스트 가장 뒤에 삽입
    result.append(str(number))
print(''.join(result)) # 리스트 -> 문자열로 변환하여 출력