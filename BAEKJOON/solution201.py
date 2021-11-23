import math

t = int(input())

for _ in range(t):
    x1,y1,r1,x2,y2,r2 = map(int, input().split())
    d = math.dist((x1,y1),(x2,y2))
    if d == 0 and r1==r2: # 두 원이 일치할 때
        print(-1)
    elif d > (r1+r2) or d < abs(r1-r2): # 두 원이 안 만남
        print(0)
    elif d == (r1+r2) or d == abs(r1-r2): # 두 원이 접할 때(외접, 내접)
        print(1)
    else: # 두 원이 두점에서 만남
        print(2)


