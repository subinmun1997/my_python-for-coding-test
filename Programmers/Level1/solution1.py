x = input()
sum_x = 0

for i in x:
    sum_x += int(i)

print("true" if int(x) % sum_x == 0 else "false")