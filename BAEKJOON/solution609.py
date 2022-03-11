import math

n, w, h = map(int, input().split())
match = [int(input()) for _ in range(n)]

max_len = math.pow(w**2 + h**2, 0.5)
for m in match:
    if m <= max_len:
        print("DA")
    else:
        print("NE")
