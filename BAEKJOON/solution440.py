number = input()

count = 0
while len(number) != 1:
    temp = 0
    for n in number:
        temp += int(n)

    count += 1
    number = str(temp)

print(count)
print("YES" if int(number)%3 == 0 else "NO")