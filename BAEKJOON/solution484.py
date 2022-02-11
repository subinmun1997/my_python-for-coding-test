t = int(input())

for _ in range(t):
    d = int(input())
    time = 0
    for i in range(1,d+1):
        t = i
        s = t*t
        if t+s <= d:
            time = i
        else:
            break
    print(time)