import math

n = 1 # 순서번호 변수
while True:
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        break
    if a == -1:
        if b>=c:
            print(f"Triangle #{n}")
            print("Impossible.")
        else:
            temp = math.pow(c, 2) - math.pow(b, 2)
            a = math.pow(temp, 0.5)
            print(f"Triangle #{n}")
            print(f"a = {a:.3f}")
    elif b == -1:
        if a>=c:
            print(f"Triangle #{n}")
            print("Impossible.")
        else:
            temp = math.pow(c, 2) - math.pow(a, 2)
            b = math.pow(temp, 0.5)
            print(f"Triangle #{n}")
            print(f"b = {b:.3f}")
    else:
        temp = math.pow(a, 2) + math.pow(b, 2)
        c = math.pow(temp, 0.5)
        print(f"Triangle #{n}")
        print(f"c = {c:.3f}")

    n += 1
    print()