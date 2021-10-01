a, b, v = map(int, input().split())

d = (v-b) / (a-b)

day = 0
if d == int(d):
    day += d
else:
    day += (d+1)

print(int(day))