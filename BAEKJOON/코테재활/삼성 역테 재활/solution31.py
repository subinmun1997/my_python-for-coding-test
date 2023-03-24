from collections import deque

def turn_right(start, dir): # 오른쪽 톱니들 회전 여부 판단 함수
    # 톱니의 개수를 넘어가거나 or 옆쪽 톱니와 현재 톱니의 극이 같다면 움직이지 않음
    if start > 4 or t[start-1][2] == t[start][6]:
        return
    if t[start-1][2] != t[start][6]: # 옆쪽 톱니와 현재 톱니의 극이 다르다면 이동
        # 오른쪽 톱니 다시 확인
        turn_right(start+1, -dir)
        # 현재 톱니 이동
        t[start].rotate(dir)

def turn_left(start, dir): # 왼쪽 톱니들 회전 여부 판단 함수
    # 톱니의 시작점 이전으로 가거나 or 옆쪽 톱니와 현재 톱니의 극이 같다면 움직이지 않음
    if start < 1 or t[start][2] == t[start+1][6]:
        return
    if t[start][2] != t[start+1][6]: # 옆쪽 톱니와 현재 톱니의 극이 다르다면 이동
        # 왼쪽 톱니 다시 확인
        turn_left(start-1, -dir)
        # 현재 톱니 이동
        t[start].rotate(dir)

# 톱니바퀴 상태 저장. 톱니 돌릴 때 rotate() 함수를 사용하기 위해 덱으로 저장
t = [deque()]
for _ in range(4):
    t.append(deque(list(map(int, input()))))

# 회전 횟수 k
k = int(input())
for _ in range(k):
    num, dir = map(int, input().split())
    # 현재 톱니가 회전하고, 오른쪽 톱니들의 회전 여부 판단. 반대로 회전하니까 -dir 대입
    turn_right(num+1, -dir)
    # 현재 톱니가 회전하고, 왼쪽 톱니들의 회전 여부 판단. 반대로 회전하니까 -dir 대입
    turn_left(num-1, -dir)
    # 현재 톱니 회전 rotate(dir): dir이 양수면 오른쪽 회전, 음수면 왼쪽 회전
    t[num].rotate(dir)

# 네 톱니의 점수의 합
result = 0
for i in range(4):
    result += (2 ** i) * t[i+1][0]

print(result)