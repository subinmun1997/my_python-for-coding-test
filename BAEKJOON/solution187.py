t = int(input())

for _ in range(t):
    data = input().split()
    num = int(data[0])

    print(data[1][:num-1]+data[1][num:])