t = int(input())
for _ in range(t):
    h, w, n = map(int, input().split())

    if n%h == 0:
        floor = h * 100
        room = n // h
    else:
        floor = (n%h) * 100
        room = n // h + 1

    print(floor + room)