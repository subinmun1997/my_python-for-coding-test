'''
문제 :  문자열 재정렬

문제 해설 :  문자열이 입력되었을 때 문자를 하나씩 확인한 뒤에, 숫자인 경우 따로 합계를 계산하고, 알파벳인 경우
             별도의 리스트에 저장한다. 그래서 결과적으로 리스트에 저장된 알파벳들을 정렬해 출력하고, 합계를 뒤에
             붙여서 출력하면 된다.
'''
data = input()
result = []
value = 0

for x in data:
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)

result.sort()

if value != 0:
    result.append(str(value))

print(''.join(result))