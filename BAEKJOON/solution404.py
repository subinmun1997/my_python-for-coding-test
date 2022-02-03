a_power, a_life = map(int, input().split())
b_power, b_life = map(int, input().split())

while True:
    a_life -= b_power
    b_life -= a_power
    if a_life <= 0 and b_life <= 0:
        print("DRAW")
        break
    elif a_life <= 0:
        print("PLAYER B")
        break
    elif b_life <= 0:
        print("PLAYER A")
        break