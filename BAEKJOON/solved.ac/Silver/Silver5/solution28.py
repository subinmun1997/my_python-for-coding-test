sticks = sorted([2**i for i in range(7)], reverse=True)

x = int(input())
count = 0
if x in sticks:
    print(1)
else:
    for stick in sticks:
        if stick <= x:
            x -= stick
            count += 1
    print(count)