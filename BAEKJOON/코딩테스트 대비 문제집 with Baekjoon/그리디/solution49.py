import sys
input = sys.stdin.readline

N = int(input())
balls = input().rstrip()
cnt = []

rexplore = balls.rstrip('R') # 오른쪽에 모여있는 'R' 제거
cnt.append(rexplore.count('R'))

rexplore = balls.rstrip('B') # 오른쪽에 모여있는 'B' 제거
cnt.append(rexplore.count('B'))

lexplore = balls.lstrip('R') # 왼쪽에 모여있는 'R' 제거
cnt.append(lexplore.count('R'))

lexplore = balls.lstrip('B') # 왼쪽에 모여있는 'B' 제거
cnt.append(lexplore.count('B'))
print(min(cnt))