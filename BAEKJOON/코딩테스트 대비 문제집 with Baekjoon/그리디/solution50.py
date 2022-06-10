import sys
input = sys.stdin.readline

n = int(input())
ball = input().strip()
cnt = []

right_r = ball.rstrip('R')
cnt.append(right_r.count('R'))

right_b = ball.rstrip('B')
cnt.append(right_b.count('B'))

left_r = ball.lstrip('R')
cnt.append(left_r.count('R'))

left_b = ball.lstrip('B')
cnt.append(left_b.count('B'))

print(min(cnt))