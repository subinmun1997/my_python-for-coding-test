'''
문제 :  왕실의 나이트

문제 해설 : 나이트가 이동할 수 있는 경로를 하나씩 확인하여 이동하면 된다.
            다만, 8x8 좌표 평면을 벗어나지 않도록 꼼꼼하게 검사하는 과정이 필요하다.
'''

n = input()
row = int(n[1])
column = int(ord(n[0])) - int(ord('a')) + 1 # ord(변수) : 아스키코드로 변환하는 함수. 아스키코드로 변환하고 a값인 97만큼 빼주고 +1 해야 해당 문자의 열 위치

move_type = [(-2,1),(-2,-1),(2,-1),(2,1),(-1,2),(1,2),(-1,-2),(1,-2)] # 나이트가 이동할 수 있는 8가지 방향 정의

result = 0
for move in move_type:
    nrow = row + move[0]
    ncolumn = column + move[1]

    if nrow >= 1 and nrow <= 8 and ncolumn >= 1 and ncolumn <= 8:
        result += 1

print(result)
