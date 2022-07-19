n = int(input())

if n < 100:
    count = n
else:
    count = 99
    for i in range(100, n+1):
        temp = []
        str_num = list(map(int, str(i)))
        temp.append(str_num[1] - str_num[0])
        temp.append(str_num[2] - str_num[1])

        if temp[0] == temp[1]:
            count += 1
print(count)