n = input()
number = [0] * 10

for i in n:
    if i == '6' or i == '9':
        if number[6] == number[9]:
            number[6] += 1
        else:
            number[9] += 1
    else:
        number[int(i)] += 1

print(max(number))