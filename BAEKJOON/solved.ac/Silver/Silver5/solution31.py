s = int(input())

temp = 1
result = 0
while True:
    s -= temp
    if s >= 0:
        temp += 1
        result += 1
    else:
        print(result)
        break