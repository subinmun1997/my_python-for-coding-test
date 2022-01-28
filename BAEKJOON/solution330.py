t = int(input())

for _ in range(t):
    yonsei = korea = 0
    for i in range(9):
        x, y = map(int, input().split())
        yonsei += x
        korea += y

    if yonsei > korea:
        print("Yonsei")
    elif korea > yonsei:
        print("Korea")
    else:
        print("Draw")