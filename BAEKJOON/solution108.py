import sys

array = []
for i in range(3):
    array.append(list(map(int, sys.stdin.readline().split())))

for i in array:
    count0 = 0
    count1 = 0
    for j in i:
        if j == 0:
            count0 += 1
        else:
            count1 += 1
    if count0 == 1:
        print("A")
    elif count0 == 2:
        print("B")
    elif count0 == 3:
        print("C")
    elif count0 == 4:
        print("D")
    else:
        print("E")

