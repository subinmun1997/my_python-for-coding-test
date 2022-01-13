n = int(input())
data = list(map(int, input().split()))
m = int(input())
req = list(map(int, input().split()))

for r in req:
    if r in data:
        print("yes")
    else:
        print("no")