t = int(input())

for _ in range(t):
    ox = input()
    result = 0
    temp = 1
    for i in ox:
        if i == 'O':
            result += temp
            temp += 1
        else:
            temp = 1
    print(result)