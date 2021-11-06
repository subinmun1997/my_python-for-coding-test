n = int(input())
items = list(map(int, input().split()))
m = int(input())
data = list(map(int, input().split()))

for i in data:
    if i in items:
        print("yes", end=' ')
    else:
        print("no", end= '')