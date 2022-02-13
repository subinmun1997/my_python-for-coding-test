import math

a, b = map(int, input().split())

a_x, a_y = math.ceil(a/4), (a%4)
if a_y == 0:
    a_y = 4

b_x, b_y = math.ceil(b/4), (b%4)
if b_y == 0:
    b_y = 4

print(abs(b_x - a_x) + abs(b_y - a_y))
