input_data = input()
row = int(input_data[1]) #입력받은 위치의 두 번째 문자를 숫자로 바꾼게 나이트가 존재하는 행 위치
column = int(ord(input_data[0])) - int(ord('a')) + 1 #ord(변수): 아스키코드로 변환하는 함수

steps = [(-2,-1),(-2,1),(2,-1),(2,1),(-1,-2),(-1,2),(1,-2),(1,2)] #행,열

result = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]

    if next_row >= 1 and next_row <=8 and next_column >= 1 and next_column <= 8: #해당 위치로 이동 가능하다면 카운트 증가
        result += 1

print(result)