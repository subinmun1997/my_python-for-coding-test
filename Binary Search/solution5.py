n = int(input())
array = input().split()

m = int(input())
target = input().split()

for i in target:
    if i in array:
        print("Yes", end=' ')
    else:
        print("No", end = ' ')