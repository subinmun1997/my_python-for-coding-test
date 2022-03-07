switch = list(input())
switch.insert(0, 'N')

count = 0
for i in range(1, len(switch)):
    if switch[i] == 'Y':
        for j in range(i, len(switch), i):
            if switch[j] == 'Y':
                switch[j] = 'N'
            else:
                switch[j] = 'Y'

        count += 1
print(count)
