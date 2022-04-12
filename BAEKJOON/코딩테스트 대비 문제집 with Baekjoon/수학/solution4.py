n = input()

if int(n) < 10:
    n = '0' + n

count = 1
value = n
n = n[1] + str((int(n[0]) + int(n[1]))%10)

while value != n:
    plus = 0
    for i in n:
        plus += int(i)
    n = n[1] + str(plus%10)
    count += 1

print(count)