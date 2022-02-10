number = list(map(int, input().split()))
number.sort()

alpha = input()
for a in alpha:
    if a == 'A':
        print(number[0], end=' ')
    elif a == 'B':
        print(number[1], end=' ')
    else:
        print(number[2], end=' ')