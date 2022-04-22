n = int(input())
product = list(map(int, input().split()))

m = int(input())
request = list(map(int, input().split()))

for i in request:
    if i in product:
        print("yes", end=' ')
    else:
        print("no", end=' ')