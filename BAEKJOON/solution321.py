h, m, s = map(int, input().split())
d = int(input())

z = d%60 #초
y = (d//60)%60 #분
x = (d//60)//60 #시

s += z
if s >= 60:
    s = s % 60
    m += 1
m += y
if m >= 60:
    m = m % 60
    h += 1
h += x
if h >= 24:
    h = h % 24

print(h, m, s)