'''
문제 :  문자열 재정렬

문제 해설 :  문자열이 입력되었을 때 문자를 하나씩 확인한 뒤에, 숫자인 경우 따로 합계를 계산하고, 알파벳인 경우
             별도의 리스트에 저장한다. 그래서 결과적으로 리스트에 저장된 알파벳들을 정렬해 출력하고, 합계를 뒤에
             붙여서 출력하면 된다.
'''
data = input()
result = []
value = 0

for x in data: # 문자를 하나씩 확인하며
    if x.isalpha(): # 알파벳인 경우 결과 리스트에 삽입
        result.append(x)
    else: # 숫자는 따로 더하기
        value += int(x)

result.sort() # 알파벳을 오름차순으로 정렬

if value != 0: # 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
    result.append(str(value))

print(''.join(result))