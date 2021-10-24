n = int(input())
data = list(input().split())
x, y = 1, 1

route = ['L','R','U','D']
dx = [0,0,-1,1] # L R U D
dy = [-1,1,0,0]

for d in data: # R R R U D D
    for i in range(4):
        if d == route[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    if nx < 1 or nx > n or ny < 1 or ny > n:
        continue
    x, y = nx, ny

print(x,y)

'''
이 문제를 요구사항대로 구현하면 연산 횟수는 이동 횟수에 비례하게 된다. 예를 들어, 이동 횟수가 
N번인 경우 시간 복잡도는 O(N)이다.

이러한 문제는 일련의 명령에 따라서 개체를 차례대로 이동시킨다는 점에서 시뮬레이션 유형으로 분류되며
구현이 중요한 대표적인 문제 유형이다.
'''

