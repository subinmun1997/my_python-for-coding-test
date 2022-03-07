import math

t = int(input())
for _ in range(t):
    n = int(input())
    start = input() # 초기 상태
    target = input() # 목표 상태

    count = 0
    b, w = 0, 0
    for i in range(len(start)):
        if start[i] != target[i]:
            if start[i] == 'B':
                b += 1
            else:
                w += 1
    if (b==0 and w>0) or (w==0 and b>0):
        print(max(b, w))
    else:
        while b == 0 or w == 0:
            count += 1
            b -= 1
            w -= 1
        count += max(b, w)
        print(count)