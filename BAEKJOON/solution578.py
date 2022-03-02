import math

n, k, p, w = map(int, input().split())
cnt = math.ceil(p/w)
print(cnt)