import math
import sys

input = sys.stdin.readline

n = int(input()) # 시험장의 개수
a = list(map(int, input().split())) # 각 시험장에 있는 응시자 수
b, c = map(int, input().split()) # 총 감독관 / 부 감독관

total = n
for i in a:
    if i < b:
        continue
    else:
        total += math.ceil((i-b)/c)

print(total)