from collections import deque

def turn_right(start, dir):
    # 4번째 톱니를 벗어나거나 or 이전 톱니와 현재 톱니의 극이 동일하다면 회전하지 않음
    if start > 4 or t[start-1][2] == t[start][6]:
        return
    # 이전 톱니와 현재 톱니의 극이 다르다면 회전함
    if t[start-1][2] != t[start][6]:
        # 현재 톱니 회전으로 인한 오른쪽 톱니 회전 여부
        turn_right(start+1, -dir)
        t[start].rotate(dir)

def turn_left(start, dir):
    # 1번째 톱니를 벗어나거나 or 옆 톱니와 현재 톱니의 극이 동일하다면 회전하지 않음
    if start < 1 or t[start][2] == t[start+1][6]:
        return
    # 옆 톱니와 현재 톱니의 극이 다르다면 회전함
    if t[start][2] != t[start+1][6]:
        # 현재 톱니 회전으로 인한 왼쪽 톱니 회전 여부
        turn_left(start-1, -dir)
        t[start].rotate(dir)

# 입력 조건: 회전할 때 rotate 함수 사용하기 위한 deque 선언
t = [deque()]
for _ in range(4):
    t.append(deque(list(map(int, input()))))

k = int(input())
for _ in range(k):
    num, dir = map(int, input().split())
    # 현재 톱니를 회전했을 때 오른쪽에 있는 톱니들에게 영향을 준다면 회전시키는 함수
    turn_right(num+1, -dir)
    # 현재 톱니를 회전했을 때 왼쪽에 있는 톱니들에게 영향을 준다면 회전시키는 함수
    turn_left(num-1, -dir)
    # 현재 톱니 회전
    t[num].rotate(dir)

result = 0
for i in range(4):
    result += (2**i) * t[i+1][0]

print(result)