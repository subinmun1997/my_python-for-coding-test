import math, sys
input = sys.stdin.readline

a, b, v = map(int, input().split())

day = 1
day += math.ceil((v-a) / (a-b))
print(day)