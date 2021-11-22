n = input()
_n = int(n)

for i in range(1, _n):
    value = 0
    value += i
    k = value
    for j in str(k):
        value += int(j)

    if value == _n:
        print(k)
        exit()

print(0)

