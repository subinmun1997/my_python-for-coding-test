'''
Implementation : 코딩 테스트에서 구현이란 '머릿속에 있는 알고리즘을 소스코드로 바꾸는 과정'이다.
                완전 탐색, 시뮬레이션 유형을 모두 '구현' 유형으로 묶어서 다루고 있다.
                완전 탐색은 모든 경우의 수를 주저 없이 다 계산하는 해결 방법을 의미하고
                시뮬레이션은 문제에서 제시한 알고리즘을 한 단계씩 차례대로 직접 수행해야 하는 문제 유형을 의미한다.

문제 : 상하좌우

문제 해설 : 이 문제를 요구사항대로 구현하면 연산 횟수는 이동 횟수에 비례하게 된다. 예를 들어 이동 횟수가 N번인 경우
            시간 복잡도는 O(N)이다.
            이러한 문제는 일련의 명령에 따라서 개체를 차례대로 이동시킨다는 점에서 시뮬레이션 유형으로 분류되며
            구현이 중요한 대표적인 문제 유형이다.

'''

n = int(input())
data = list(input().split())
x, y = 1, 1

dx = [0,0,-1,1] # L R U D에 다른 이동 방향
dy = [-1,1,0,0]
move_type = ['L','R','U','D']

for i in data:
    for j in range(len(move_type)):
        if i == move_type[j]:
            nx = x + dx[j]
            ny = y + dy[j]
    if nx < 1 or nx > n or ny < 1 or ny > n: # 공간을 벗어나는 경우 무시
        continue
    x, y = nx, ny

print(x,y)