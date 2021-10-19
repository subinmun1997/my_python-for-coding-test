n = input()
count = 0

for i in n:
    count+=1
    print(i, end='')
    if count%10 == 0:
        print()