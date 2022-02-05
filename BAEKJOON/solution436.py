n = input()

check = 0
for i in range(1, len(n)):
    x, y = n[:i], n[i:]
    mul_x = mul_y = 1
    for k in x:
        mul_x *= int(k)
    for j in y:
        mul_y *= int(j)

    if mul_x == mul_y:
        check = 1
        break

print("YES" if check else "NO")
