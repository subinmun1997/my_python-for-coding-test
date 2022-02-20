def check(maxShape):
    a_max, b_max = a[1:].count(maxShape), b[1:].count(maxShape)
    if a_max == b_max:
        if maxShape == 1:
            return 'D'
        else:
            return check(maxShape-1)
    elif a_max > b_max:
        return 'A'
    else:
        return 'B'

n = int(input())

for _ in range(n):
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    maxA, maxB = max(a[1:]), max(b[1:])
    if maxA != maxB:
        if maxA > maxB:
            print('A')
        else:
            print('B')
    else:
        print(check(maxA))