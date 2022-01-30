for i in range(int(input())):
    val = bin(int(input()))[2:][::-1]

    for i,v in enumerate(val):
        if v == '1':
            print(i, end=' ')
    print()