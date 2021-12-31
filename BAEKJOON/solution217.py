camp, day = 0, 1

while True:
    l, p, v = map(int, input().split())
    if l == p == v == 0:
        break
    camp = (v // p) * l
    temp = v % p
    if temp > l:
        camp += l
    else:
        camp += temp

    print("Case %d: %d" %(day, camp))
    day += 1
