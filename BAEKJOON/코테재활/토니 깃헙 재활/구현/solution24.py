'''
문제 아이디어

달력의 시작일자에 +1 종료일자+1 에 -1을 해주었다.
해당 일자의 누적합이 사각형의 높이가 될 것이다.
그리고 1~366까지 누적합을 확인하면서 가로,세로 크기의 최대값을 갱신했다.

누적합 간단 설명
해당 날에 0이 아닌 경우 사각형 가로 길이를 증가시키고, 높이를 최대값으로 갱신하자.
해당 날이 만약 0이라면 사각형의 넓이를 계산하고 가로,세로 길이를 0으로 초기화하자.
'''

n = int(input())
calendar = [0] * 367
for _ in range(n):
    s, e = map(int, input().split())
    calendar[s] += 1
    calendar[e + 1] -= 1

width = 0
height = 0
answer = 0
for i in range(1, 367):
    calendar[i] += calendar[i - 1]
    if calendar[i] == 0:
        answer += width * height
        width = 0
        height = 0
    else:
        width += 1
        height = max(height, calendar[i])

print(answer)