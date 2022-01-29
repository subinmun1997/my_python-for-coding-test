n = int(input())
tele = list(map(int, input().split()))

y = m = 0
for t in tele:
    y += (t//30+1) * 10
    m += (t//60+1) * 15

if y < m:
    print("Y %d" %(y))
elif m < y:
    print("M %d" %(m))
else:
    print("Y M %d" %(y))