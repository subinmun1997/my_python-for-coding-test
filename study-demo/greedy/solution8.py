s = input()

result = 0
for i in s:
    if result <= 1 or int(i) <= 1:
        result += int(i)
    else:
        result *= int(i)

print(result)