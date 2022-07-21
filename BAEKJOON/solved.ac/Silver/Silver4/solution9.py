n = int(input())
lst = set(map(int, input().split()))
m = int(input())
num = list(map(int, input().split()))

for i in num:
    print(1 if i in lst else 0)