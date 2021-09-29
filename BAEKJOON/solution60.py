def d(n):
    not_make = []
    for i in range(1,10001):
        a = list(map(int, str(i)))
        i += sum(a)
        if i not in not_make and i <= 10000:
            not_make.append(i)

    for p in range(n, 10001):
        if p not in not_make:
            print(p)

d(1)