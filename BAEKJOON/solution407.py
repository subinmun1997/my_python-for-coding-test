sticks = [2**i for i in range(7)]
sticks.sort(reverse=True)

x = int(input())
if x in sticks:
    print(1)
else:
    count = 0
    for stick in sticks:
        if stick <= x:
            x -= stick
            count += 1

    print(count)