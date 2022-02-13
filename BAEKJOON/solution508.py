import math

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

answer_x, answer_y = (x1*y2 + x2*y1),(y1*y2)
gcd = math.gcd(answer_x, answer_y)

print(answer_x//gcd, answer_y//gcd)