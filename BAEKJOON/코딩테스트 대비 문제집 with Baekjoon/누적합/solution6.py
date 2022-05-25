import sys
input = sys.stdin.readline

n = int(input())
number = list(map(int, input().split()))

answer = 0
sum_x = 0
for num in number:
    answer += num * sum_x
    sum_x += num

print(answer)